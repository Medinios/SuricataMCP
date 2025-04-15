import asyncio
import os
from typing import Any

import config
from CommandExecutionError import CommandExecutionError
from mcp.server.fastmcp import FastMCP


# Create an MCP server
mcp = FastMCP("SuricataMCP")


async def run_cmd(cmd_args: list[str], timeout: int = 300)-> dict[str, int | None | bool | Any] | str:
    suricata_full_path = os.path.join(config.SURICATA_DIR, config.SURICATA_EXE_FILE)

    try:
        process = await asyncio.create_subprocess_exec(
            suricata_full_path,
            *cmd_args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
        except asyncio.TimeoutError:
            process.kill()
            await process.wait()
            raise CommandExecutionError(
                message=f"Command timed out after {timeout} seconds",
                exit_code=None
            )

        stdout_decoded = stdout.decode().strip()
        stderr_decoded = stderr.decode().strip()

        if process.returncode != 0:
            raise CommandExecutionError(
                message="Non-zero exit code",
                exit_code=process.returncode,
                stdout=stdout_decoded,
                stderr=stderr_decoded
            )

        return stdout_decoded


    except FileNotFoundError:
        raise CommandExecutionError(message=f"Command not found: {' '.join(cmd_args)}")
    except Exception as e:
        raise CommandExecutionError(message=str(e))


@mcp.tool()
async def get_suricata_version() -> dict[str, int | None | bool | Any] | str:
    return await run_cmd(["-V"])

@mcp.tool()
async def get_suricata_help() -> dict[str, int | None | bool | Any] | str:
    return await run_cmd(["-h"])

@mcp.tool()
async def get_alerts_from_pcap_file(pcap_destination: str, destination_folder_results:str) -> dict[str, int | None | bool | Any] | str:
    try:
        await run_cmd(["-r", f'{pcap_destination}', "-l", f'{destination_folder_results}'])
        with open(destination_folder_results + "/fast.log", 'r', encoding='utf-8') as log_file:
            log_contents = log_file.read()
            return log_contents
    except FileNotFoundError:
        raise CommandExecutionError(f"Log file not found at {destination_folder_results}")
    except Exception as e:
        raise CommandExecutionError(f"An error occurred: {e}")


if __name__ == "__main__":
    print("🚀 Starting Suricata MCP Server")
    print(f"📂 Suricata directory: {config.SURICATA_DIR}")
    mcp.run(transport="stdio")
