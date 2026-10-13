// AI Literacy Open Lab: small, accessible client-side interactions.
document.addEventListener('DOMContentLoaded', () => {
  // FAQ: keep the accordion tidy by allowing one answer open at a time.
  const faqItems = Array.from(document.querySelectorAll('.faq-item'));
  faqItems.forEach((item) => {
    item.addEventListener('toggle', () => {
      if (!item.open) return;
      faqItems.forEach((other) => {
        if (other !== item) other.open = false;
      });
    });
  });

  // Resource search: filters the resource cards by title, description, and keywords.
  const query = document.getElementById('resource-query');
  const clear = document.getElementById('resource-clear');
  const cards = Array.from(document.querySelectorAll('#resource-list .resource-card'));
  const count = document.getElementById('search-count');
  const noResults = document.getElementById('no-results');

  if (!query || !cards.length) return;
  const normalize = (value) => value.toLocaleLowerCase('ja').normalize('NFKC').trim();
  const filterCards = () => {
    const term = normalize(query.value);
    let visible = 0;
    cards.forEach((card) => {
      const text = normalize(`${card.textContent} ${card.dataset.search || ''}`);
      const matches = !term || text.includes(term);
      card.hidden = !matches;
      if (matches) visible += 1;
    });
    if (count) count.textContent = `資料 ${visible} 件`;
    if (noResults) noResults.hidden = visible !== 0;
  };
  query.addEventListener('input', filterCards);
  if (clear) clear.addEventListener('click', () => {
    query.value = '';
    filterCards();
    query.focus();
  });
  filterCards();
});
