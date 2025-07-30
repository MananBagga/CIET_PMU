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


let currentStep = 1;
const totalSteps = 5;


const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

function updateProgressBar() {
    const percent = ((currentStep - 1) / (totalSteps - 1)) * 100;
    document.getElementById("progress-bar").style.width = percent + "%";
    document.getElementById("progress-text").textContent = `Step ${currentStep} of ${totalSteps}`;
}

function showStep(step) {
    document.querySelectorAll(".form-step").forEach(div => div.classList.add("hidden"));
    document.getElementById(`form-step-${step}`).classList.remove("hidden");
    currentStep = step;
    updateProgressBar();
    updateRemoveButtons(step);
}

function validateStep(stepToShow) {
    const stepForm = document.getElementById(`form-step-${currentStep}`);
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
}

function nextStep(step) { validateStep(step); }
function previousStep(step) { showStep(step); }

function addEntry(type) {
    const entriesDiv = document.getElementById(`${type}-entries`);
    const newEntry = entriesDiv.querySelector(`.${type}-entry`).cloneNode(true);

    newEntry.querySelectorAll("input").forEach(input => {
        input.value = "";
        input.classList.remove("border-red-500");
    });

    entriesDiv.appendChild(newEntry);
    updateRemoveButtons(currentStep);
}

function removeEntry(button, type) {
    const entriesDiv = document.getElementById(`${type}-entries`);
    const entryDiv = button.closest(`.${type}-entry`);
    const entryId = button.dataset.entryId;


    if (entriesDiv.querySelectorAll(`.${type}-entry`).length <= 1) {
        alert("At least one entry is required.");
        return;
    }


    entryDiv.remove();


    if (entryId) {
        fetch(`/delete-subentry/${entryId}/`, {
            method: "DELETE",
            headers: { "X-CSRFToken": csrftoken }
        })
        .then(response => response.json())
        .then(data => { if (!data.success) alert("Error deleting entry from DB"); })
        .catch(() => alert("Request failed."));
    }

    updateRemoveButtons(currentStep);
}

function updateRemoveButtons(step) {
    const entryTypes = ["kpi", "workshop", "meeting", "manpower"];
    const type = entryTypes[step - 2];
    if (!type) return;

    document.querySelectorAll(`#${type}-entries .${type}-entry .remove-btn`)
        .forEach(btn => btn.classList.remove("hidden"));
}


document.addEventListener("DOMContentLoaded", () => {
    updateProgressBar();
    showStep(1);
    updateRemoveButtons(currentStep);
});


window.nextStep = nextStep;
window.previousStep = previousStep;
window.validateStep = validateStep;
window.addEntry = addEntry;
window.removeEntry = removeEntry;

