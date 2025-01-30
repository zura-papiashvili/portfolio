document.addEventListener("DOMContentLoaded", function () {
    const codeSnippet = document.getElementById("code-snippet").querySelector("pre");
    const code = [
        { text: "const", class: "keyword" },
        { text: " myPortfolio", class: "variable" },
        { text: " = ", class: "" },
        { text: "'Web Dev'", class: "string" },
        { text: ";", class: "" },
        { text: "\n", class: "" },
        { text: "function", class: "keyword" },
        { text: " createWebsite()", class: "function" },
        { text: " {", class: "" },
        { text: "\n  ", class: "" },
        { text: "return", class: "variable" },
        { text: " 'Interactive Portfolio'", class: "string" },
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