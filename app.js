document.addEventListener('DOMContentLoaded', () => {
  const panel20 = document.getElementById('panel20');
  const paperCountEl = document.getElementById('paper-count');
  const lastUpdatedEl = document.getElementById('last-updated');

  // 1️⃣ 加载卡片 HTML
  fetch('./generate_cards/card.html', { cache: 'no-cache' })
    .then(res => {
      if (!res.ok) throw new Error(`Failed to load: ${res.status}`);
      return res.text();
    })
    .then(html => {
      panel20.innerHTML = html;
    })
    .catch(err => {
      panel20.innerHTML = `<p class="load-error">无法加载卡片<br>${err.message}</p>`;
    });

  // 2️⃣ 加载统计数据
  fetch('./generate_cards/stats.json', { cache: 'no-cache' })
    .then(res => {
      if (!res.ok) throw new Error(`Failed to load stats: ${res.status}`);
      return res.json();
    })
    .then(data => {
      // 更新文章总数
      if (paperCountEl) {
        paperCountEl.textContent = data.num_papers;
      }
      // 更新最后更新时间
      if (lastUpdatedEl) {
        lastUpdatedEl.textContent = data.last_updated;
      }
    })
    .catch(err => {
      console.error('无法加载 stats.json:', err);
      if (paperCountEl) {
        paperCountEl.textContent = 'N/A';
      }
      if (lastUpdatedEl) {
        lastUpdatedEl.textContent = 'N/A';
      }
    });
});
