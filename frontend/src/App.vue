<script setup>
import { RouterLink, RouterView } from 'vue-router'

const navLinks = [
  { to: '/', label: 'Home' },
  { to: '/players', label: 'Players' },
  { to: '/teams', label: 'Teams' },
  { to: '/comments', label: 'Comments' },
  { to: '/about', label: 'About' },
]
</script>

<template>
  <div class="app-shell">
    <header class="site-header">
      <RouterLink class="brand" to="/">
        <span class="brand-mark">SF</span>
        <span class="brand-text">StatFoot</span>
      </RouterLink>

      <nav class="site-nav" aria-label="Main navigation">
        <RouterLink v-for="link in navLinks" :key="link.to" :to="link.to">
          {{ link.label }}
        </RouterLink>
      </nav>
    </header>

    <main class="page">
      <RouterView />
    </main>
  </div>
</template>
