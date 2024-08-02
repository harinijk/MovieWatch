<template>
  <div>
    <header>
      <router-link to="/">
        <h1><span>Your</span>Movies</h1>
      </router-link>
      <router-link to="/liked-movies" class="liked-movies-link">Likes</router-link>
    </header>
    <main>
      <router-view/>
    </main>
  </div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;700&display=swap');
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Fira Sans', sans-serif;

  &::selection {
    background: transparentize($color: #aa79cb, $amount: 0.5);
  }
}

body {
  background-color: #35495E;
}

a {
  text-decoration: none;
}

header {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 16px;
  background-color: #2C3D4E;
  box-shadow: 0px 0px 6px rgba(0,0,0,0.1);

  h1 {
    color: white;
    font-size: 28px;
    span {
      color: rgb(224, 79, 127);
    }
  }

  .liked-movies-link{
    color:white;
    margin-left: auto;
  }
}
</style>
