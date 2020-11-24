<template>
  <div id="snipet-card">
    <span
      v-for="(sequence, sequence_index) in snipet"
      v-bind:key="'x' + sequence_index"
    >
      <span v-if="sequence_index < compareStartIndex">
        {{ sequence }}
      </span>
    </span>
    <div
      v-for="(sequence, sequence_index) in snipet"
      v-bind:key="sequence_index"
    >
      <div v-if="sequence_index >= compareStartIndex">
        <p>{{ columns[sequence_index] }}</p>
        <div class="code-area">
          <code>{{ sequence }}</code>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SinpetCard",
  props: {
    columns: {
      type: Array,
      default: function () {
        return ["Category", "Content", "Detail", "Python", "JavaScript"];
      },
    },
    snipet: {
      type: Array,
      default: function () {
        return ["A", "B", "C", "==", "==", "==="];
      },
    },
  },
  data() {
    return {
      compareStartIndex: 3,
    };
  },
};
</script>

<style lang="css" scoped>
#snipet-card {
  background-color: antiquewhite;
  margin: 8% auto; /* 15% from the top and centered */
  padding: 20px;
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

#snipet-card .code-area {
  background-color: white;
  padding: 1em;
}
</style>