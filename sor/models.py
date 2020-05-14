"""Models for sor api app
"""
from django.db import models


class Label(models.Model):
    """A label or tag for servers
    """

    name = models.CharField(max_length=25, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = "Labels"

    def __str__(self):
        return self.name


class Owner(models.Model):
    """Represents the owner of the server or a resource
    """

    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"

    def __str__(self):
        return self.name


class Cluster(models.Model):
    """Represents a cluster of servers grouped together
    """

    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"

    def __str__(self):
        return self.name


class Environment(models.Model):
    """Represents an environment for the server
    """

    class Category(models.TextChoices):
        DEVELOP = "DEV", "Development"
        TESTING = "BETA", "Testing"
        STAGING = "STAGE", "Staging"
        PRODUCTION = "PROD", "Production"

    name = models.CharField(max_length=25, unique=True)
    category = models.CharField(
        max_length=5, choices=Category.choices, default=Category.DEVELOP
    )
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Environment"
        verbose_name_plural = "Environments"

    def __str__(self):
        return self.name


class Domain(models.Model):
    """Domain name servers for servers
    """

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        DECOM = "DECOM", "Decom"

    name = models.CharField(max_length=253, unique=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(
        Owner, related_name="domains", on_delete=models.PROTECT
    )
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=8, choices=Status.choices, default=Status.ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    """Represents installed operating system in servers
    """

    class Family(models.TextChoices):
        LINUX = "LINUX", "Linux"
        UNIX = "UNIX", "Unix"
        WINDOWS = "WINDOWS", "Windows"

    class Architecture(models.TextChoices):
        X86 = "32", "X86"
        X64 = "64", "X64"

    name = models.CharField(max_length=100)
    family = models.CharField(
        max_length=7, choices=Family.choices, default=Family.LINUX
    )
    architecture = models.CharField(
        max_length=2, choices=Architecture.choices, default=Architecture.X64
    )
    version = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Operating System"
        verbose_name_plural = "Operating Systems"

    def __str__(self):
        return self.name


class Server(models.Model):
    """Represents a server running on-prem or cloud
    """

    class Category(models.TextChoices):
        MAIL = "MAIL", "Mail Server"
        FTP = "FTP", "FTP Server"
        WEB = "WEB", "Web Server"
        PROXY = "PROXY", "Proxy Server"
        APP = "APP", "Application Server"
        BUILD = "BUILD", "Build Server"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        DECOM = "DECOM", "Decom"

    name = models.CharField(max_length=25, unique=True)
    ip_address = models.GenericIPAddressField(
        verbose_name="IP Address", unique=True
    )
    category = models.CharField(
        max_length=5, choices=Category.choices, default=Category.WEB
    )
    owner = models.ForeignKey(
        Owner, related_name="servers", on_delete=models.PROTECT
    )
    domain = models.ForeignKey(
        Domain, related_name="servers", on_delete=models.PROTECT
    )
    cluster = models.ForeignKey(
        Cluster,
        related_name="servers",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    environments = models.ManyToManyField(Environment, related_name="servers")
    operating_system = models.ForeignKey(
        OperatingSystem, related_name="servers", on_delete=models.PROTECT
    )
    labels = models.ManyToManyField(Label, related_name="servers")
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=8, choices=Status.choices, default=Status.INACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"

    def __str__(self):
        return self.name

    @property
    def fqdn(self):
        """Returns fully qualified domain name of server
        """
        return "{name}.{domain}".format(
            name=self.name, domain=self.domain.name
        )


class Product(models.Model):
    """Represents the products hosted in servers
    """

    name = models.CharField(max_length=50, unique=True)
    port = models.IntegerField(null=True, blank=True)
    version = models.CharField(max_length=20)
    owner = models.ForeignKey(
        Owner, related_name="products", on_delete=models.PROTECT
    )
    link = models.URLField(null=True, blank=True)
    repository = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
