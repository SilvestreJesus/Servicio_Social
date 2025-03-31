<template>
  <header>
    <h1>{{ titulo }}</h1>
  </header>

  <section id="content">
    <div class="text">
      <p v-html="texto"></p>
    </div>
    <img :src="muyalImage" alt="muyal">
  </section>
  
  <div ref="formula" class="formula1"></div>
  <div ref="formula2" class="formula2"></div>
  
  <section class="fondo">
    <div class="title-left">weights associated with risk calculation</div>
    <div class="row-space-temp">
      <div class="space-container">
        <div class="title">Space:</div>
        <select v-model="selectedSpace" class="form-control-left">
          <option v-for="(state, index) in estados" :key="index" :value="state">
            {{ state }}
          </option>
        </select>
      </div>

      <div class="temp-container">
        <div class="title">Temporary:</div>
        <input type="range" class="form-control-range" min="2004" max="2022" v-model="selectedYear" />
        <div class="range-text">Selected Year: {{ selectedYear }}</div>
      </div>
    </div>
    

    <div class="colum-left">
      <div v-for="(value, key) in indicator" :key="key" class="col-md-3">
        <label :for="key" class="form-label">{{ key.toUpperCase() }}</label>
        <input type="number" class="form-control pesos" :id="key" v-model="indicator[key]" step="0.01" min="0" max="1" />
      </div>
    </div>

    <div class="risk">
      <h2 id="riskValue">Press the button to see the index</h2>
      <button id="btnRisk" class="run"></button>
    </div>    

    
    <form id="sustanciasForm" class="form-container">
     
      <div class="columns">
        <div class="column" v-for="(sustanciasGroup, index) in [sustanciasIzquierda, sustanciasDerecha]" :key="index">
          <div v-for="(sustancia, idx) in sustanciasGroup" :key="idx">
            <label :for="sustancia.cas" class="form-label">{{ sustancia.name }}</label>
            <input type="number" class="form-control sustancia" :id="sustancia.cas" v-model="sustancia.valor" step="0.01" min="0" max="1" @input="validateSums" @change="validateSums" />
          </div>
        </div>
      </div>
    </form>
  </section>
</template>

  <script>
  import axios from 'axios';
  import muyalImage from "../assets/muyal-ilal-logo.png";
  import katex from 'katex'; 
  import 'katex/dist/katex.min.css';
  
  export default {
  data() {
    return {
      titulo: "Space-time proximity indicator to carcinogenic substances (IARC) C50 cancer precursors (SSI)",
      muyalImage,
      texto: `The Silent Spring Institute has identified 216 chemicals linked to breast tumors in animals.
              Of these, 73 are in consumer products or foods, 35 are in the air, and 25 are in occupational exposures
              affecting more than 5,000 women annually. For more information, visit the 
              <a href="https://silentspring.org/project/mammary-carcinogens-list" target="_blank">
              Silent Spring Institute Mammary Carcinogens List</a>. 
              A linear statistical risk model is shown below where importance weights are assigned to the 17 chemicals 
              to calculate the risk per year and state in the Mexican Republic.`,
      
      selectedYear: 2013,
      indicator: {
        vol: 0.25,
        iarc: 0.25,
        dof: 0.25,
        prox: 0.25
      },
      weights: "weights associated with risk calculation",
      sustancias: [],
      estados: [],
      selectedSpace: null,
    };
  },
  computed: {
    sustanciasIzquierda() {
      return this.sustancias.filter((_, index) => index % 2 === 0);
    },
    sustanciasDerecha() {
      return this.sustancias.filter((_, index) => index % 2 !== 0);
    }
  },
  mounted() {
    axios.get("http://127.0.0.1:5000/api/sustancias")
    .then(response => {
      this.sustancias = response.data.sustancias.map(sustancia => ({
      ...sustancia,
      valor: (1 / 17).toFixed(2)
    }));
    this.estados = response.data.estados;
  })
  .catch(error => {
    console.error("Error fetching data:", error);
  });
     
  katex.render(
    'IPS(S_{iss}) = \\sum_{i=1}^{17} \\omega_i v_i',
    this.$refs.formula,
    { throwOnError: false }
  );
  katex.render(
    'v_i = f(x_i) = \\omega_1 Vol(x_i, t, p) + \\omega_2 Diff(x_i,\\hat{y_i},t,p) + f(IARC_{X_i}, t) + d(p,E)',
    this.$refs.formula2,
    { throwOnError: false }
  );
}
};

</script>
  