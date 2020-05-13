"""Serializers for SOR api app models
"""
from rest_framework import serializers
from rest_framework.utils import model_meta
from rest_framework.exceptions import ValidationError

from sor.models import (
    Label,
    Owner,
    Cluster,
    Environment,
    Domain,
    OperatingSystem,
    Server,
    Product,
)


class ManyToOneRelatedField(serializers.Field):
    def to_representation(self, related_field):
        return related_field.name

    def to_internal_value(self, data):
        if not isinstance(data, str):
            msg = "Incorrect Type. Expected a str but got %s" % (
                type(data).__name__
            )
            raise ValidationError([msg])

        if not data:
            msg = "%s value cannot be empty" % (self.field_name)
            raise ValidationError([msg])

        return data


class ManyToManyRelatedField(serializers.Field):
    def to_representation(self, related_field):
        return [item.name for item in related_field.all()]

    def to_internal_value(self, data):
        if not isinstance(data, list):
            msg = "Incorrect Type. Expected a list but got %s" % (
                type(data).__name__
            )
            raise ValidationError([msg])

        if not all(isinstance(item, str) for item in data):
            msg = "Incorrect Value Type. Expected %s value in str type" % (
                self.source
            )
            raise ValidationError([msg])

        return data


class LabelSerializer(serializers.ModelSerializer):
    """Serializes Label model
    """

    class Meta:
        model = Label
        fields = [
            "id",
            "name",
        ]


class OwnerSerializer(serializers.ModelSerializer):
    """Serializes Owner model
    """

    class Meta:
        model = Owner
        fields = [
            "id",
            "name",
            "email",
            "description",
        ]


class ClusterSerializer(serializers.ModelSerializer):
    """Serializes Cluster model
    """

    class Meta:
        model = Cluster
        fields = [
            "id",
            "name",
            "description",
        ]


class EnvironmentSerializer(serializers.ModelSerializer):
    """Serializes Environment model
    """

    class Meta:
        model = Environment
        fields = [
            "id",
            "name",
            "category",
            "description",
        ]


class DomainSerializer(serializers.ModelSerializer):
    """Serializes Domain model
    """

    owner = ManyToOneRelatedField()

    class Meta:
        model = Domain
        fields = [
            "id",
            "name",
            "location",
            "owner",
            "description",
            "status",
        ]

    def create(self, validated_data):
        return Domain.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def validate_owner(self, value):
        try:
            owner = Owner.objects.get(name=value)
        except Owner.DoesNotExist:
            msg = "Owner %s matching query does not exist" % value
            raise ValidationError([msg])
        return owner


class OperatingSystemSerializer(serializers.ModelSerializer):
    """Serializes OperatingSystem model
    """

    class Meta:
        model = OperatingSystem
        fields = [
            "id",
            "name",
            "family",
            "architecture",
            "version",
        ]


class ServerSerializer(serializers.ModelSerializer):
    """Serializes Server model
    """

    owner = ManyToOneRelatedField()
    domain = ManyToOneRelatedField()
    cluster = ManyToOneRelatedField()
    environments = ManyToManyRelatedField()
    operating_system = ManyToOneRelatedField()
    labels = ManyToManyRelatedField()

    class Meta:
        model = Server
        fields = [
            "id",
            "name",
            "ip_address",
            "category",
            "owner",
            "domain",
            "cluster",
            "environments",
            "operating_system",
            "labels",
            "description",
            "status",
        ]

    def create(self, validated_data):
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}

        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        instance = ModelClass._default_manager.create(**validated_data)

        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance

    def update(self, instance, validated_data):
        model_field_info = model_meta.get_field_info(instance)

        many_to_many_fields = []

        for attr, value in validated_data.items():
            if (
                attr in model_field_info.relations
                and model_field_info.relations[attr].to_many
            ):
                many_to_many_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()

        for attr, value in many_to_many_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance

    def validate_owner(self, value):
        try:
            owner = Owner.objects.get(name=value)
        except Owner.DoesNotExist:
            msg = "Owner %s matching query does not exist" % value
            raise ValidationError([msg])
        return owner

    def validate_domain(self, value):
        try:
            domain = Domain.objects.get(name=value)
        except Domain.DoesNotExist:
            msg = "Domain %s matching query does not exist" % value
            raise ValidationError([msg])
        return domain

    def validate_cluster(self, value):
        try:
            cluster = Cluster.objects.get(name=value)
        except Cluster.DoesNotExist:
            msg = "Cluster %s matching query does not exist" % value
            raise ValidationError([msg])
        return cluster

    def validate_environments(self, value):
        environments = []

        for environment_name in value:
            try:
                environments.append(
                    Environment.objects.get(name=environment_name)
                )
            except Environment.DoesNotExist:
                msg = (
                    "Environment %s matching query does not exist"
                    % environment_name
                )
                raise ValidationError([msg])
        return environments

    def validate_operating_system(self, value):
        try:
            operating_system = OperatingSystem.objects.get(name=value)
        except OperatingSystem.DoesNotExist:
            msg = "OperatingSystem %s matching query does not exist" % value
            raise ValidationError([msg])
        return operating_system

    def validate_labels(self, value):
        labels = []

        for label_name in value:
            try:
                labels.append(Label.objects.get(name=label_name))
            except Label.DoesNotExist:
                msg = "Label %s matching query does not exist" % label_name
                raise ValidationError([msg])
        return labels


class ProductSerializer(serializers.ModelSerializer):
    """Serializes Product model
    """

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "port",
            "version",
            "owner",
            "link",
            "repository",
        ]
