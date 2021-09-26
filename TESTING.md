# Testing #

[Main README.md file](https://github.com/MihaelaVacarus/bojeaux_ms4/blob/main/README.md)

View the live project [here](https://bojeaux-ms4.herokuapp.com/).

### **Contents** ###

- [Automated Testing](#automated-testing)
    - [W3C Markup Validator](#w3c-markup-validator)
    - [W3C CSS Validation Service](#w3c-css-validation-service)
    - [Flake8](#flake8)
    - [JSHint](#jshint)
    - [Chrome DevTools Lighthouse](#chrome-devtools-lighthouse)
    - [Responsive Viewer](#responsive-viewer)
    - [Mobile Friendly Test Google Search Console](#mobile-friendly-test-google-search-console)
    - [WEB accessibility by Level Access](#web-accessibility-by-level-access)

- [Manual Testing](#manual-testing)
    - [Testing User Stories](#testing-user-stories)
    - [Testing Functionalities](#testing-functionalities)
        - [Devices Used for Testing](#devices-used-for-testing)
        - [Further Manual Testing](#further-manual-testing)

- [Bugs](#bugs)

### [W3C Markup Validator](https://validator.w3.org/)
Run on all pages and passed with no errors/warnings.


### [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
Run on CSS code and no errors returned, just a few warnings that relate to browser prefixes and that can be safely ignored.

### [Flake8](https://flake8.pycqa.org/en/latest/index.html)
Run the Python code validator and fixed most issues. The unfixed ones I researched and learned it's fine to leave as they are.

### [JSHint](https://jshint.com/)
Run the JSHint validator and fixed all errors.

### [Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse)
- For Mobile the scores are: 
    - Performance: 71
    - Accessibility: 95
    - Best Practices: 87
    - SEO: 83
- For Desktop the scores are:
    - Performance: 97
    - Accessibility: 79
    - Best Practices: 87
    - SEO: 80

### [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)
- I ran the extension on each page of the website and responsiveness checks OK. 

### [Mobile Friendly Test Google Search Console](https://search.google.com/test/mobile-friendly)
- The result is that the page is mobile friendly.

### [WEB accessibility by Level Access](https://www.webaccessibility.com/)
- The compliance result score is 94%.