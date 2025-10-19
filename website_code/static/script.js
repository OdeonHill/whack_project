// ============================
// Phone Savings Progress Logic
// ============================

document.addEventListener("DOMContentLoaded", () => {
  const fill = document.getElementById("fill");
  const percentage = document.getElementById("percentage");
  const motivation = document.getElementById("motivation");
  const happyGif = document.getElementById("happyGif");
  const veryAngyGif = document.getElementById("veryAngyGif");

  // Utility: safely show only the relevant mood image
  function showMood(progress) {
    happyGif.style.display = "none";
    veryAngyGif.style.display = "none";

    if (progress > 0) {
      motivation.textContent = "You're doing great! Keep saving! 💪";
      happyGif.style.display = "block";
    } else {
      motivation.textContent = "Let's get started! Save your first £ today! 💸";
      veryAngyGif.style.display = "block";
    }
  }

  // Core: fetch user savings progress from Flask route
  async function updateFill() {
    try {
      const response = await fetch("/savings_progress");
      const data = await response.json();

      // If there’s no savings record yet
      if (!data.has_savings) {
        fill.style.height = "0%";
        percentage.textContent = "0% saved";
        showMood(0);
        return;
      }

      const progress = Math.min(data.progress, 100); // cap at 100
      fill.style.height = progress + "%";
      percentage.textContent = `${progress}% saved`;
      showMood(progress);
    } catch (error) {
      console.error("Error fetching savings progress:", error);
      motivation.textContent = "Error loading data 😕";
    }
  }

  // Initial call and periodic refresh
  updateFill();
  setInterval(updateFill, 5000);
});
