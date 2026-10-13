(() => {
  const input = document.getElementById('resource-query');
  const clear = document.getElementById('resource-clear');
  const cards = Array.from(document.querySelectorAll('.resource-card'));
  const count = document.getElementById('search-count');
  const empty = document.getElementById('no-results');
  if (!input || !clear || !count || !empty) return;

  const normalize = (value) => value.toLocaleLowerCase().normalize('NFKC').trim();
  const filterResources = () => {
    const query = normalize(input.value);
    const terms = query.split(/\s+/).filter(Boolean);
    let visible = 0;
    cards.forEach((card) => {
      const searchable = normalize(`${card.textContent} ${card.dataset.search || ''}`);
      const matches = terms.every((term) => searchable.includes(term));
      card.hidden = !matches;
      if (matches) visible += 1;
    });
    count.textContent = query ? `検索結果 ${visible} 件` : `資料 ${visible} 件`;
    empty.hidden = visible !== 0;
  };
  input.addEventListener('input', filterResources);
  clear.addEventListener('click', () => {
    input.value = '';
    filterResources();
    input.focus();
  });
  filterResources();
})();
