  // Показать/скрыть кнопку-стрелку в зависимости от позиции прокрутки
  window.addEventListener('scroll', function () {
    var scrollToTopButton = document.getElementById('scroll-to-top');
    if (scrollY > 100) {
        scrollToTopButton.style.display = 'block';
    } else {
        scrollToTopButton.style.display = 'none';
    }
});

// Плавная прокрутка наверх при клике на кнопку-стрелку
document.getElementById('scroll-to-top').addEventListener('click', function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});