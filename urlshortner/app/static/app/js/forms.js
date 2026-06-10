document.querySelectorAll('input[name="expires_at"]').forEach((input) => {
    const rawValue = input.value;
    input.type = 'datetime-local';

    if (rawValue) {
        const normalizedValue = rawValue.replace(' ', 'T').slice(0, 16);
        const parsedDate = new Date(normalizedValue);

        if (!Number.isNaN(parsedDate.getTime())) {
            const localDate = new Date(parsedDate.getTime() - parsedDate.getTimezoneOffset() * 60000);
            input.value = localDate.toISOString().slice(0, 16);
        } else {
            input.value = normalizedValue;
        }
    } else {
        input.value = '';
    }

    input.placeholder = 'Select date and time';
});