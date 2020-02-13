<template>
 <section>

  <div>
    <v-app-bar
      color="deep-purple accent-4"
      dense
      dark
    >
      <v-app-bar-nav></v-app-bar-nav>

      <v-toolbar-title>Dados</v-toolbar-title>

    </v-app-bar>
    </div>

    <v-form >
        <v-container>
            <v-row>
                <v-col cols="10" sm="5" md="3">
                <v-text-field label="Faça sua busca aqui" solo v-model="pesquisa"></v-text-field>
                </v-col>
                <v-icon>fas fa-search</v-icon>
            </v-row>
        </v-container>   
    </v-form>     

    <v-spacer></v-spacer>
    <v-simple-table fixed-header height="700px">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Data</th>
          <th class="text-left">Nota Fiscal</th>
          <th class="text-left">Transportadora</th>
          <th class="text-left">Placa</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="dado in consulta" :key="dado.id">
          <td>{{ dado.data }}</td>
          <td>{{ dado.nota_fiscal }}</td>
          <td>{{ dado.transportadora }}</td>
          <td>{{ dado.placa }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
   
</section>
</template>
<script>

import axios from 'axios'
export default {
    
 name: 'Dados',
 data() {
  return {
   dados: [],
   pesquisa: '',
  }
 },
 computed: {
     consulta(){
         return this.dados.filter( dado => {
            return dado.transportadora.toLowerCase().indexOf(this.pesquisa.toLowerCase()) > -1 || dado.data.toLowerCase().indexOf(this.pesquisa.toLowerCase()) > -1
            || dado.nota_fiscal.toLowerCase().indexOf(this.pesquisa.toLowerCase()) > -1 || dado.placa.toLowerCase().indexOf(this.pesquisa.toLowerCase()) > -1
             })
     }
 },
 created() {
  this.all();
 },
 methods: {
  all () {
   axios.request({
    baseURL: 'http://localhost:8000',
    method: 'get',
    url: '/api/dados/'
   }).then( response => {
     this.dados = response.data
   });
  },
 }
}
</script>