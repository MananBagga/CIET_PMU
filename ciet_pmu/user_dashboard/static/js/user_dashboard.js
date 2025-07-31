function openEditForm(programId, programType, programTitle, programBudget, createdAt) {
    console.log("hello");
    
    document.getElementById('program-id').value = programId;
    document.getElementById('program-details').innerHTML = `
      <p><strong>Program Type:</strong> ${programType}</p>
      <p><strong>Program Title:</strong> ${programTitle}</p>
      <p><strong>Budget:</strong> ₹${programBudget}</p>
      <p><strong>Created At:</strong> ${createdAt}</p>
    `;
    document.getElementById('edit-form').classList.remove('hidden');
    document.getElementById('form-step-1').classList.remove('hidden');
    for (let i = 2; i <= 5; i++) {
      document.getElementById(`form-step-${i}`).classList.add('hidden');
    }
  }

  function nextStep(step) {
    for (let i = 1; i <= 5; i++) {
      document.getElementById(`form-step-${i}`).classList.add('hidden');
    }
    document.getElementById(`form-step-${step}`).classList.remove('hidden');
  }




// -------------------------------------------------------------------------------------------------------------





let currentStep = 1;
const totalSteps = 5;


function updateProgressBar() {
    const percent = ((currentStep - 1) / (totalSteps - 1)) * 100;
    const bar = document.getElementById("progress-bar");
    const text = document.getElementById("progress-text");
    if (bar && text) {
        bar.style.width = percent + "%";
        text.textContent = `Step ${currentStep} of ${totalSteps}`;
    }
}


window.showStep = function (step) {
    document.querySelectorAll(".form-step").forEach(div => div.classList.add("hidden"));
    const stepDiv = document.getElementById(`form-step-${step}`);
    if (stepDiv) stepDiv.classList.remove("hidden");

    currentStep = step;
    updateProgressBar();
    updateRemoveButtons(step);
};

window.validateStep = function (stepToShow) {
    const stepForm = document.getElementById(`form-step-${currentStep}`);
    if (!stepForm) return;

    const requiredFields = stepForm.querySelectorAll("[required]");
    let allFilled = true;

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add("border-red-500");
            allFilled = false;
        } else {
            field.classList.remove("border-red-500");
        }
    });

    if (allFilled) {
        showStep(stepToShow);
    } else {
        alert("Please fill in all required fields.");
    }
};

window.nextStep = step => validateStep(step);
window.previousStep = step => showStep(step);



window.addEntry = function (type) {
    const entriesDiv = document.getElementById(`${type}-entries`);
    if (!entriesDiv) return;

    const template = entriesDiv.querySelector(`.${type}-entry`);
    if (!template) return;

    const newEntry = template.cloneNode(true);
    newEntry.querySelectorAll("input").forEach(input => {
        input.value = "";
        input.classList.remove("border-red-500");
    });

    // Remove old IDs from cloned entry
    newEntry.querySelectorAll("[data-entry-id]").forEach(btn => btn.removeAttribute("data-entry-id"));

    entriesDiv.appendChild(newEntry);
    updateRemoveButtons(currentStep);
};

window.removeEntry = function (button, type) {
    const entriesDiv = document.getElementById(`${type}-entries`);
    if (!entriesDiv) return;

    const entries = entriesDiv.querySelectorAll(`.${type}-entry`);
    const entryDiv = button.closest(`.${type}-entry`);
    const entryId = button.dataset.entryId;

    if (entries.length > 1) {
        entryDiv.remove();
        updateRemoveButtons(currentStep);
    } else {
        alert("At least one entry is required.");
    }

    // Delete from database if entryId exists
    if (entryId) {
        const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        fetch(`/delete-subentry/${entryId}/`, {
            method: "DELETE",
            headers: { "X-CSRFToken": csrftoken }
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) alert("Error deleting entry from DB");
        })
        .catch(() => alert("Request failed."));
    }
};



function updateRemoveButtons(step) {
    const entryTypes = ["kpi", "workshop", "meeting", "manpower"];
    const type = entryTypes[step - 2];
    if (!type) return;

    const entriesDiv = document.getElementById(`${type}-entries`);
    if (!entriesDiv) return;

    entriesDiv.querySelectorAll(`.${type}-entry`).forEach(entry => {
        const btn = entry.querySelector(".remove-btn");
        if (btn) btn.classList.remove("hidden");
    });
}



document.addEventListener("DOMContentLoaded", () => {
    updateProgressBar();
    showStep(1);
    updateRemoveButtons(currentStep);
});


// ---------------------------------------------------------------------------------



  function toggleSummary(programId) {
    const allSummaries = document.querySelectorAll('[id^="summary-"]');
    allSummaries.forEach((div) => {
      if (div.id !== `summary-${programId}`) {
        div.classList.add("hidden");
      }
    });

    const summaryDiv = document.getElementById(`summary-${programId}`);
    summaryDiv.classList.toggle("hidden");
  }