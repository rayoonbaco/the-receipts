const filters = document.querySelectorAll('.filter');
const cards = document.querySelectorAll('.project-card');

filters.forEach((button) => {
  button.addEventListener('click', () => {
    filters.forEach((item) => item.classList.remove('active'));
    button.classList.add('active');
    const selected = button.dataset.filter;
    cards.forEach((card) => {
      const categories = card.dataset.category.split(' ');
      card.hidden = selected !== 'all' && !categories.includes(selected);
    });
  });
});

const copyButton = document.querySelector('.copy-prompt');
const copyStatus = document.querySelector('.copy-status');

copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(copyButton.dataset.copy);
    copyStatus.textContent = 'Copied. Paste it into the AI reviewer of your choice.';
  } catch {
    copyStatus.textContent = 'Press and hold the question above to copy it.';
  }
});
