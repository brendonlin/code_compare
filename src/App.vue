<template>
  <div id="app">
    <Header></Header>
    <CompareTable></CompareTable>
    <!-- <SnipetCard></SnipetCard> -->
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import CompareTable from "./components/CompareTable.vue";
export default {
  name: "App",
  components: {
    Header,
    CompareTable,
  },
};
</script>