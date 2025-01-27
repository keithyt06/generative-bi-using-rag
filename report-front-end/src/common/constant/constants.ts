export const CHATBOT_NAME = "GenBI Chatbot";

export const DEFAULT_USER_INFO = {
  userId: "",
  displayName: "",
  loginExpiration: +new Date() + 6000,
  isLogin: false,
};

export const DEFAULT_QUERY_CONFIG = {
  selectedLLM: "",
  selectedDataPro: "",
  intentChecked: true,
  complexChecked: true,
  answerInsightChecked: false,
  contextWindow: false,
  modelSuggestChecked: false,
  temperature: 0.1,
  topP: 1,
  topK: 250,
  maxLength: 2048,
};

export const LOCALSTORAGE_KEY = "__GEN_BI_STORE_INFO__";

export const BACKEND_URL = process.env.VITE_BACKEND_URL?.endsWith("/")
  ? process.env.VITE_BACKEND_URL
  : process.env.VITE_BACKEND_URL + "/";

export const APP_TITLE = process.env.VITE_TITLE;

export const APP_LOGO = process.env.VITE_LOGO || "";

export const APP_RIGHT_LOGO = process.env.VITE_RIGHT_LOGO || "";

export const SQL_DISPLAY = process.env.VITE_SQL_DISPLAY;

// TODO: decide whether to add an env var for this style switch?
// https://cloudscape.design/patterns/general/density-settings/
export const COMPACT_STYLE = true;
