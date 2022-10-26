
<template>
    <table class="table">
      <thead>
        <th>date</th>
        <th>name</th>
        <th>count_iron</th>
        <th>count_silicon</th>
        <th>count_aluminum</th>
        <th>count_calcium</th>
        <th>count_sulfur</th>
      </thead>
      <tbody>
        <tr v-for="row in back_data" :key="row.id" @dblclick="$data.back_data_row = row">
          <td>{{row.date}}</td>
          <td>{{row.name}}</td>
          <td>{{row.count_iron}}</td>
          <td>{{row.count_silicon}}</td>
          <td>{{row.count_aluminum}}</td>
          <td>{{row.count_calcium}}</td>
          <td>{{row.count_sulfur}}</td>
          <td><button class="btn btn-outline-danger btn-sm mx-1" @click="deleteRow(row)">x</button></td>
        </tr>
      </tbody>
    </table>

    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="back_data_row.name">
        <input type="text" class="form-control col-3 mx-2" placeholder="count_iron" v-model="back_data_row.count_iron">
        <input type="text" class="form-control col-3 mx-2" placeholder="count_silicon" v-model="back_data_row.count_silicon">
        <input type="text" class="form-control col-3 mx-2" placeholder="count_aluminum" v-model="back_data_row.count_aluminum">
        <input type="text" class="form-control col-3 mx-2" placeholder="count_calcium" v-model="back_data_row.count_calcium">
        <input type="text" class="form-control col-3 mx-2" placeholder="count_sulfur" v-model="back_data_row.count_sulfur">
        <input type="datetime-local" class="form-control col-3 mx-2" placeholder="date" v-model="back_data_row.date">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>



</template>

<script>


export default {
  name: 'App',
  components: {
  },
  data(){
    return {
      back_data_row: {},
      back_data: []
    }
  },
  async created() {
      await this.fetchData();
  },
  methods: {
    submitForm() {
      if (this.back_data_row.id === undefined)
      {
        this.createBackDataRow();
      }else{
        this.editBackDataRow();
      }
    },
    async fetchData(){
      var response =  await fetch('http://127.0.0.1:8000/datalist/');
      this.back_data = await response.json();
    },
    async createBackDataRow(){

      await this.fetchData();

      this.back_data_row.date = this.back_data_row.date.split("T")[0];

      await fetch('http://127.0.0.1:8000/datalist/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.back_data_row)
      });

      await this.fetchData();

    },
    async editBackDataRow(){
      await this.fetchData();

      this.back_data_row.date = this.back_data_row.date.split("T")[0];

      await fetch(`http://127.0.0.1:8000/datalist/${this.back_data_row.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.back_data_row)
      });

      await this.fetchData();
      this.back_data_row = {};
    },
    async deleteRow(row) {
      await this.fetchData();

      this.back_data_row.date = this.back_data_row.date.split("T")[0];

      await fetch(`http://127.0.0.1:8000/datalist/${row.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.back_data_row)
      });

      await this.fetchData();
    }
  },
};
</script>