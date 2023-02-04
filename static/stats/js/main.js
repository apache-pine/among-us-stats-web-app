const now = new Date();

const currentYear = now.getFullYear();

const currentDay = now.getDay();

const theHour = now.getHours();

const fullDate = new Intl.DateTimeFormat("en-US", {dateStyle: "full"}).format(now);

document.querySelector(".currentYear").textContent = currentYear;

const lastModif = new Date(document.lastModified);

document.querySelector(".lastModif").textContent = `Last Updated: ${lastModif.toLocaleString()}`;