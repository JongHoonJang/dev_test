<template>
  <NavBarView />
  <router-view  class="body"/>
</template>

<script>
import NavBarView from '@/components/NavBarView';

export default {
  components: { NavBarView },
};
</script>

<style>
.body {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
}
body {
  margin: 0;
}
#app {   
  width : 100vw;
  height : 100vh;

}
head {
  margin: 0;
}

</style>