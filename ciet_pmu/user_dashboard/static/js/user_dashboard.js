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