# Ross Buddy
Ross Buddy consists of two Docker containers

* The first container will run a DCMTK [`storescp`](https://support.dcmtk.org/docs/storescp.html) 
  process that will simply save any incoming DICOM files to an incoming directory as fast as possible. 
* The second container will run a [`dicomsorter`](https://github.com/harvard-nrg/dicomsorter) 
  process that will sort the DICOM files into a meaningful folder structure with meaningful file 
  names.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

### Configuration

Default and sample environment variables are provided in the `default.env` file. 
Add these variables to your environment or simply copy `default.env` to `.env`. 
Values in this file are used to populate dollar-notation variables in the 
`docker-compose.yml` file.

> [!Important]
> The `UID` and `GID` fields determine the user and group who will run the containers and 
> who will own processes that will save and sort files within `INCOMING_DIR`. These must 
> match a user with sufficient privileges on the host operating system.

|     Option           | Description                                                         |
|----------------------|---------------------------------------------------------------------|
| INCOMING_DIR         | Host path to save incoming DICOM files (will be mounted to `/data`) |
| UID                  | Container user UID                                                  |
| GID                  | Container user GID                                                  |
| SLACK_CHANNEL        | Slack channel to post messages                                      |
| SLACK_BOT_TOKEN      | Slack Bot OAuth2 Token                                              |
| SLACK_DISABLE        | Disable Slack messages                                              |
| SUPERVISOR_LOG_FILE  | Container path to save supervisord log                              |
| STORESCP_AE_TITLE    | `storescp` AE Title                                                 |
| STORESCP_PORT        | `storescp` port                                                     |
| STORESCP_LOG_FILE    | Container path to save `storescp` process log                       |
| STORESCP_LOG_LEVEL   | Log level for `storescp` process                                    |
| DICOMSORTER_LOG_FILE | Container path to save `dicomsorter` log                            |

### Building

Once you have populated your [Configuration](#Configuration), you can build the 
Ross Buddy containers 

> [!Note]
> This step is not entirely necessary. Attempting to [start](#Starting) the 
> containers will trigger a build if the containers haven't been built yet.

```shell
docker compose build
```

### Starting

To run the Ross Buddy containers, you can use `docker compose up`

> [!Note]
> The `-d|--detach` argument will run the containers in the background

```shell
docker compose up -d
```

### Stopping

To tear down the containers, you can run `docker compose down`

```shell
docker compose down
```

### Monitoring

You can monitor logs saved to locations defined in the [Configuration](#Configuration) file
or monitor container logs using `docker compose logs`

> [!Note]
> The `-f|--follow` argument will show the container logs in real time

```bash
docker compose logs -f
```

## License

`rossbuddy` is distributed under the terms of the [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) license.

