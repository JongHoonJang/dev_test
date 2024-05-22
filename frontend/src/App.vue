<template>
  <NavBarView />
  <router-view />
</template>

<script>
import NavBarView from '@/components/NavBarView';

export default {
  components: { NavBarView },
};
</script>