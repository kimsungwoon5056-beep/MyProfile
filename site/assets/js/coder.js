(() => {
  const key = 'colorscheme';
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  const choices = ['light', 'dark', 'auto'];
  const labels = { light: '밝은 화면', dark: '어두운 화면', auto: '기기 설정' };
  let preference = 'auto';
  let saved = true;
  try {
    const value = localStorage.getItem(key);
    if (choices.includes(value)) preference = value;
  } catch (_) { saved = false; }

  function render() {
    const theme = preference === 'auto' ? (media.matches ? 'dark' : 'light') : preference;
    document.body.classList.remove('colorscheme-auto', 'colorscheme-light', 'colorscheme-dark', 'preload-transitions');
    document.body.classList.add('colorscheme-' + theme);
    document.documentElement.style.colorScheme = theme;
    document.querySelectorAll('[data-theme-choice]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.themeChoice === preference));
    });
    const status = document.getElementById('screen-settings-status');
    if (status) status.textContent = '선택: ' + labels[preference] + (saved ? '' : ' (이 브라우저에서는 저장할 수 없어 현재 페이지에서만 적용됩니다.)');
  }

  document.querySelectorAll('[data-theme-choice]').forEach(button => {
    button.addEventListener('click', () => {
      preference = button.dataset.themeChoice;
      try { localStorage.setItem(key, preference); saved = true; }
      catch (_) { saved = false; }
      render();
    });
  });
  media.addEventListener('change', () => { if (preference === 'auto') render(); });
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) {
      preference = choices.includes(event.newValue) ? event.newValue : 'auto';
      render();
    }
  });
  render();
})();
