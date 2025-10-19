document.addEventListener("DOMContentLoaded", () => {
  const fill = document.getElementById("fill");
  const percentage = document.getElementById("percentage");
  const motivation = document.getElementById("motivation");
  const happyGif = document.getElementById("happyGif");
  const veryAngyGif = document.getElementById("veryAngyGif");
  const savingsForm = document.getElementById("savings-form");
  const amountInput = document.getElementById("amount");
  const message = document.getElementById("update-message");

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

  async function updateFill() {
    try {
      const response = await fetch("/savings_progress");
      const data = await response.json();

      if (!data.has_savings) {
        fill.style.height = "0%";
        percentage.textContent = "0% saved";
        showMood(0);
        return;
      }

      const progress = Math.min(data.progress, 100);
      fill.style.height = progress + "%";
      percentage.textContent = `${progress}% saved`;
      showMood(progress);
    } catch (error) {
      console.error("Error fetching savings progress:", error);
      motivation.textContent = "Error loading data 😕";
    }
  }

  // Submit form to add to savings
  savingsForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const amount = parseFloat(amountInput.value);
    if (!amount || amount <= 0) return;

    try {
      const res = await fetch("/add_savings", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ amount }),
      });

      const data = await res.json();
      if (data.success) {
        message.textContent = "Savings updated successfully!";
        amountInput.value = "";
        updateFill(); // refresh the phone fill
      } else {
        message.textContent = "Failed to update savings.";
      }
    } catch (err) {
      console.error("Error adding savings:", err);
      message.textContent = "Error updating savings.";
    }
  });

  updateFill();
  setInterval(updateFill, 5000);
});
