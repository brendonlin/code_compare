<template>
  <div>
    <h1>代码对比(CODE COMPARE)</h1>

    <menu id="tap-menu">
      <ul>
        <li
          v-for="(item, key) in menuItems"
          v-bind:key="key"
          v-bind:class="{ selected: item.status == 1 }"
          v-on:click="setItemSelected(item)"
          v-bind:style="{ display: item.enable == 1 ? 'inline' : 'none' }"
        >
          {{ item.name }}
        </li>
      </ul>
    </menu>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      menuItems: [
        {
          name: "编程语言",
          status: 1,
          enable: 1,
        },
        {
          name: "数据库语言",
          status: 0,
          enable: 0,
        },
        {
          name: "数据类型",
          status: 0,
          enable: 0,
        },
      ],
    };
  },
  methods: {
    setItemSelected(item) {
      for (var x of this.menuItems) {
        if (x.name == item.name) {
          x.status = 1;
        } else {
          x.status = 0;
        }
      }
    },
  },
};
</script>

<style lang="css" scoped>
#tap-menu {
  margin: 0;
  padding: 0;
}
#tap-menu ul {
  display: flex;
  padding: 0 0 0 0em;
}

#tap-menu ul li {
  list-style: none;
  margin-right: 8px;
  padding: 0.4em;
  cursor: pointer;
  border: 2px solid rgba(0, 0, 0, 0);
  border-radius: 6px;
}

#tap-menu ul li:hover {
  border-bottom: 1px solid rgba(238, 176, 96, 0.5);
}

#tap-menu ul li.selected {
  /* background-color: rgb(161 160 187); */
  border-bottom: 3px solid rgba(238, 176, 96, 0.5);
}
</style>