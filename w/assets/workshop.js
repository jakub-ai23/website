/* ============================================================
   Workshop page behaviour  -  jakubpopluhar.com/w/
   Click-to-copy prompt blocks, single-open accordions, sidebar
   scroll-spy. Pure vanilla, no dependencies. Include with `defer`.
   ============================================================ */
(function () {
  // Copy prompt on click
  document.querySelectorAll('.prompt-block').forEach(block => {
    block.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(block.textContent.trim());
        block.classList.add('copied');
        setTimeout(() => block.classList.remove('copied'), 1500);
      } catch (e) {
        const range = document.createRange();
        range.selectNodeContents(block);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
      }
    });
  });

  // Accordion: only one <details> open at a time within an .exercise
  document.querySelectorAll('.exercise').forEach(exercise => {
    const allDetails = exercise.querySelectorAll(':scope > details');
    allDetails.forEach(det => {
      det.addEventListener('toggle', () => {
        if (det.open) {
          allDetails.forEach(sib => { if (sib !== det && sib.open) sib.open = false; });
        }
      });
    });
  });

  // Sidebar active state on scroll
  const navLinks = document.querySelectorAll('.sidebar-nav a');
  const sectionIds = Array.from(navLinks).map(a => a.getAttribute('href').slice(1));
  const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);
  if (sections.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          navLinks.forEach(link => link.classList.toggle('active', link.getAttribute('href') === '#' + id));
        }
      });
    }, { rootMargin: '-25% 0px -65% 0px' });
    sections.forEach(s => observer.observe(s));
  }
})();
