<template>
  <div class="p-6">
    <input
      type="text"
      v-model="keyword"
      className="rounded border-2 bg-white border-gray-200 w-full h-12 pl-2"
      placeholder="Search for Meals"
      @change="searchMeals"
    />
  </div>
  <div>
    <pre>{{ meals }}</pre>
  </div>
</template>

<script setup>
import { computed } from "@vue/reactivity";
import { ref } from "vue";
import store from "../store";

const keyword = ref("");
const meals = computed(() => store.state.searchedMeals);

function searchMeals() {
  if (keyword.value) {
    store.dispatch("searchMeals", keyword.value);
  } else {
    store.commit("setSearchedMeals", []);
  }
}
</script>
