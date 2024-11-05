function calculateSettingAsThemeString({ localStorageTheme, systemSettingDark }) {
  if (localStorageTheme !== null) {
    return localStorageTheme;
  }

  if (systemSettingDark.matches) {
    return "dark";
  }

  return "light";
}

function updateThemeOnHtmlEl(theme) {
  document.querySelector("html").setAttribute("data-theme", theme);
}

// On page load
const toggleSwitch = document.querySelector(".theme-switch input");
const localStorageTheme = localStorage.getItem("theme");
const systemSettingDark = window.matchMedia("(prefers-color-scheme: dark)");
let currentTheme = calculateSettingAsThemeString({ localStorageTheme, systemSettingDark });
updateThemeOnHtmlEl(currentTheme);

toggleSwitch.addEventListener("change", () => {
  const newTheme = currentTheme === "light" ? "dark" : "light";

  localStorage.setItem("theme", newTheme);
  updateThemeOnHtmlEl(newTheme);

  currentTheme = newTheme;
});
