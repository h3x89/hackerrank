import { existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";
import { receive } from "../node_modules/probot/lib/bin/receive.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const base = resolve(__dirname, "../node_modules");
const appPath = existsSync(resolve(base, "probot-settings/index.js"))
  ? resolve(base, "probot-settings/index.js")
  : resolve(base, "@probot/settings/index.js");

const args = [
  "-e",
  "repository.created",
  "-p",
  process.env.GITHUB_EVENT_PATH,
  appPath,
];

receive(args).catch((error) => {
  console.error(error);
  process.exit(1);
});
