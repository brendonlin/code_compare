<template>
  <div>
    <div
      class="modal"
      v-bind:style="{ display: modalDisplay }"
      v-on:click="hideShow"
    >
      <SnipetCard
        v-bind:snipet="selectSnipet"
        v-bind:columns="dataframe.columns"
        v-on:click="1"
        class="modal-content"
      ></SnipetCard>
    </div>
    <table id="code-compare-table">
      <colgroup>
        <col class="compare-category" />
        <col class="compare-content" />
        <col class="compare-detail" />
        <col class="python" />
        <col class="java" />
        <col class="javascript" />
        <col class="dart" />
        <col class="rlang" />
      </colgroup>
      <thead>
        <tr>
          <th v-for="(value, index) in dataframe.columns" v-bind:key="index">
            {{ value }}
          </th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="(row, row_index) in dataframe.rows"
          v-on:click="showRow(row_index)"
          v-bind:key="row_index"
        >
          <td
            nowrap="true"
            v-for="(cell, cell_index) in row"
            v-bind:key="cell_index"
          >
            <code v-if="cell_index >= compareStartIndex">
              {{ limitString(cell) }}
            </code>
            <span v-else>
              {{ cell }}
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import tableData from "../assets/table.json";
import tableData from "../assets/code_compare.json";
import SnipetCard from "./SnipetCard.vue";

export default {
  name: "CompareTable",
  data() {
    return {
      name: "",
      compareStartIndex: 3,
      dataframe: tableData,
      selectSnipet: ["Alpha", "Beta", "Gammer", "==", "==", "==="],
      modalDisplay: "none",
      // dataframe: {
      //   columns: ["Category", "Content", "Detail", "Python", "JavaScript"],
      //   rows: [
      //     [
      //       "数据类型",
      //       "字符串",
      //       "字符串大写",
      //       "$(string).upper()",
      //       "$(string).toUpperCase()",
      //     ],
      //     [
      //       "数据类型",
      //       "字符串",
      //       "字符串长度",
      //       "len($(string))",
      //       "$(string).length",
      //     ],
      //   ],
      // },
    };
  },
  methods: {
    limitString(string) {
      var strlen = string.length;
      if (strlen >= 30) {
        return string.slice(0, 27) + "...";
      } else {
        return string;
      }
    },
    showRow(rowIndex) {
      this.selectSnipet = this.dataframe.rows[rowIndex];
      this.modalDisplay = "block";
    },
    hideShow(e) {
      var clickedElement = e.target;
      if (!clickedElement.closest(".modal-content")) {
        this.modalDisplay = "none";
      }
    },
  },
  components: {
    SnipetCard,
  },
};
</script>

<style lang="css" scoped>
#code-compare-table {
  table-layout: fixed;
}
#code-compare-table tbody tr:hover {
  background-color: rgba(250, 235, 215, 0.5);
  cursor: pointer;
}

#code-compare-table td {
  border-top: 1px solid grey;
  margin: 0;
  text-align: center;
}

#code-compare-table thead {
  padding: 0;
}

.python {
  background-color: rgba(71, 132, 212, 0.5);
}

.java {
  background-color: rgba(255, 0, 0, 0.5);
}

.javascript {
  background-color: rgba(221, 209, 46, 0.5);
}

.dart {
  background-color: rgb(57 79 187 / 49%);
}

.rlang {
  background-color: rgba(173, 216, 230, 0.486);
}

.modal {
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
}
</style>