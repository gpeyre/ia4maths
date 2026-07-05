<template>
  <div class="footer-shell">
    <div class="footer-progress">
      <span :style="{ width: `${($slidev.nav.currentPage / $slidev.nav.total) * 100}%` }" />
    </div>
    <div class="footer-mark">
      <span>AI for Theory · Gabriel Peyré</span>
      <span>{{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}</span>
    </div>
  </div>
</template>
