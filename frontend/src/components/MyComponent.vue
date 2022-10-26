<template>
    <div ref="sheetEl" />
  </template>
  <script>
  import { ref, onMounted } from "vue";
  import jspreadsheet from "jspreadsheet";
  import "jspreadsheet/dist/jspreadsheet.css";
  import "jsuites/dist/jsuites.css";
  export default {
    name: "MyComponent",
    props: {
      options: {
        type: Object,
        require: true,
      },
    },
    setup(props) {
      const options = props.options ? { ...props.options } : {};
      const sheetEl = ref(null);
      onMounted(() => {
        jspreadsheet(sheetEl.value, options);
      });
      return { sheetEl };
    },
  };
  </script>