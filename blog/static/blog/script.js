document.addEventListener("DOMContentLoaded", function () {
    const codeSnippet = document.getElementById("code-snippet").querySelector("pre");
    const code = [
        { text: "const", class: "keyword" },
        { text: " newWebsite", class: "variable" },
        { text: " = ", class: "" },
        { text: "'Web Dev'", class: "string" },
        { text: ";", class: "" },
        { text: "\n", class: "" },
        { text: "function", class: "keyword" },
        { text: " createWebsite()", class: "function" },
        { text: " {", class: "" },
        { text: "\n  ", class: "" },
        { text: "return", class: "variable" },
        { text: " 'Special Website For You!'", class: "string" },
        { text: ";", class: "" },
        { text: "\n}", class: "" }
    ];

    let index = 0;

    function typeCode() {
        if (index < code.length) {
            const span = document.createElement("span");
            span.className = code[index].class;
            span.innerText = code[index].text;

            codeSnippet.appendChild(span);
            index++;

            // Add a slight delay before typing the next piece of code
            setTimeout(typeCode, 100);
        }
    }

    setTimeout(typeCode, 2500); // Delay code typing until bars are fully visible
});


// Smooth Scroll to FAQ section
document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('data-bs-target'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Accordion Toggle Animation
const accordions = document.querySelectorAll('.accordion-button');
accordions.forEach((accordion) => {
    accordion.addEventListener('click', function () {
        // Add smooth fade-in effect for the accordion body
        const body = this.closest('.accordion-item').querySelector('.accordion-collapse');
        if (body.classList.contains('collapse')) {
            body.classList.add('show');
            body.style.transition = "max-height 0.5s ease-in-out";
            body.style.maxHeight = "500px";  // Limit height for transition
        } else {
            body.style.maxHeight = "0";
            setTimeout(() => body.classList.remove('show'), 500);
        }

        // Highlight the active FAQ
        document.querySelectorAll('.accordion-button').forEach(button => {
            button.classList.remove('active-faq');
        });
        this.classList.add('active-faq');
    });
});


