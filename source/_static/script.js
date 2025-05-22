document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".spoiler").forEach((el) => {
      el.addEventListener("click", () => {
        el.classList.toggle("revealed");
      });
    });
  });