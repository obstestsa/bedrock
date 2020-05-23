<template>
  <v-container fluid>
    <BreadCrumbs :breadCrumbs="breadCrumbs" />
    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          prepend-inner-icon="mdi-magnify"
          label="Search"
          clearable
          hide-details
          class="pb-1"
        ></v-text-field>
        <v-spacer />
        <v-dialog v-if="isAuthenticated" v-model="dialog" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn class="mx-2" depressed v-on="on">
              ADD
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      v-model="editedItem.name"
                      label="Name*"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field
                      v-model="editedItem.ip_address"
                      label="IP Address*"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select
                      v-model="editedItem.category"
                      :items="['Mail', 'FTP', 'Web', 'Proxy', 'Application']"
                      label="Category*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12">
                    <v-select
                      v-model="editedItem.operating_system"
                      :items="[
                        'Microsoft Windows Server 2012 R2',
                        'Microsoft Windows Server 2018',
                        'Ubuntu 18 LTS',
                        'Redhat Server 8',
                        'CentOS Server 8',
                      ]"
                      label="Operating System*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select
                      v-model="editedItem.domain"
                      :items="['AWS', 'ONPREM']"
                      label="Domains*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select
                      v-model="editedItem.cluster"
                      :items="['CILIN', 'CIWIN', 'CORNERSTONEWEB']"
                      label="Cluster*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="editedItem.environment"
                      :items="['DEVELOP', 'BETA', 'STAGING', 'PRODUCTION']"
                      label="Emvronment*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="editedItem.owner"
                      :items="['DevOps', 'IT', 'DBA']"
                      label="Owner*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="editedItem.status"
                      :items="['Active', 'Inactive', 'Decomissioned']"
                      label="Status*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12">
                    <v-textarea
                      v-model="editedItem.description"
                      label="Description"
                      rows="1"
                    ></v-textarea>
                  </v-col>
                </v-row>
              </v-container>
              <small>* indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn color="blue darken0-1" text @click="close">Cancel</v-btn>
              <v-btn color="blue darken0-1" text @click="save">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-switch class="mx-2" label="Small" v-model="dense"></v-switch>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="getServers"
        :search="search"
        :single-expand="singleExpand"
        :expanded.sync="expanded"
        :loading="isLoading"
        :loading-text="loadingText"
        :dense="dense"
        item-key="name"
        show-expand
        class="elevation-1"
      >
        <template v-slot:item.status="{ item }">
          <v-chip :small="dense" :color="getStatusColor(item.status)" dark>{{
            item.status
          }}</v-chip>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)">
            mdi-pencil
          </v-icon>
          <v-icon small class="mr-2" @click="deleteItem(item.id)">
            mdi-delete
          </v-icon>
        </template>
        <template v-slot:expanded-item="{ headers, item }">
          <td :colspan="headers.length">{{ item.description }}</td>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';
import {
  FETCH_RESOURCES,
  RESOURCE_CREATE,
  RESOURCE_UPDATE,
  RESOURCE_DELETE,
} from '../store/actions.type';
import BreadCrumbs from '../components/BreadCrumbs';

export default {
  name: 'Server',
  components: {
    BreadCrumbs,
  },
  data: () => ({
    breadCrumbs: ['Home', 'Sor', 'Server'], // TODO: Make breadCrumbs dynamic
    loadingText: 'Loading Servers, Please wait.',
    dense: false,
    dialog: false,
    expanded: [],
    singleExpand: true,
    search: '',
    headers: [
      { text: 'Name', align: 'start', value: 'name' },
      { text: 'IP Address', value: 'ip_address' },
      { text: 'Category', value: 'category' },
      { text: 'Owner', value: 'owner' },
      { text: 'Domain', value: 'domain' },
      { text: 'Cluster', value: 'cluster' },
      { text: 'Environment', value: 'environment' },
      { text: 'Operating System', value: 'operating_system' },
      { text: 'Status', value: 'status', align: 'center' },
    ],
    servers: [],
    editedIndex: -1,
    editedItem: {
      name: '',
      ip_address: '',
      category: '',
      owner: '',
      domain: '',
      cluster: '',
      environment: '',
      operating_system: '',
      status: '',
      description: '',
    },
    defaultItem: {
      name: '',
      ip_address: '',
      category: '',
      owner: '',
      domain: '',
      cluster: '',
      environment: '',
      operating_system: '',
      status: '',
      description: '',
    },
  }),
  created() {
    this.fetchResources('servers');
    if (this.isAuthenticated) {
      this.headers.push({
        text: 'Actions',
        value: 'actions',
        sortable: false,
      });
    }
    this.headers.push({ text: '', value: 'data-table-expand' });
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Server' : 'Edit Server';
    },
    ...mapGetters({
      getServers: 'getServers',
      isLoading: 'isLoading',
      isAuthenticated: 'isAuthenticated',
    }),
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
  },
  methods: {
    editItem(item) {
      this.editedIndex = this.getServers.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(id) {
      confirm('Are you sure you want to delete this item?') &&
        this.removeResource({ type: 'servers', id: id });
    },

    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      if (this.editedIndex > -1) {
        this.updateResource({
          type: 'servers',
          resource: this.editedItem,
        });
      } else {
        this.createResource({
          type: 'servers',
          resource: this.editedItem,
        });
      }
      this.close();
    },

    getStatusColor(status) {
      if (status === 'Active') return 'green';
      else if (status === 'Inactive') return 'orange';
      else return 'red';
    },
    ...mapActions({
      fetchResources: FETCH_RESOURCES,
      createResource: RESOURCE_CREATE,
      updateResource: RESOURCE_UPDATE,
      removeResource: RESOURCE_DELETE,
    }),
  },
};
</script>

<style></style>
