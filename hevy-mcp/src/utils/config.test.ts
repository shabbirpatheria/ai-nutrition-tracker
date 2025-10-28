import { describe, expect, it } from "vitest";
import { parseConfig } from "./config.js";

function env(vars: Record<string, string | undefined>): NodeJS.ProcessEnv {
	return { ...process.env, ...vars } as NodeJS.ProcessEnv;
}

describe("parseConfig", () => {
	it("prefers --hevy-api-key= over env", () => {
		const cfg = parseConfig(
			["--hevy-api-key=cliKey"],
			env({ HEVY_API_KEY: "envKey" }),
		);
		expect(cfg.apiKey).toBe("cliKey");
	});

	it("supports bare hevy-api-key= form", () => {
		const cfg = parseConfig(["hevy-api-key=bareKey"], env({}));
		expect(cfg.apiKey).toBe("bareKey");
	});

	it("falls back to env HEVY_API_KEY", () => {
		const cfg = parseConfig([], env({ HEVY_API_KEY: "envOnly" }));
		expect(cfg.apiKey).toBe("envOnly");
	});

	it("detects http transport via --http", () => {
		const cfg = parseConfig(["--http"], env({ HEVY_API_KEY: "k" }));
		expect(cfg.transportMode).toBe("http");
	});

	it("detects http transport via env", () => {
		const cfg = parseConfig(
			[],
			env({ MCP_TRANSPORT: "http", HEVY_API_KEY: "k" }),
		);
		expect(cfg.transportMode).toBe("http");
	});
});
