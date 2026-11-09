# 1. Access & SSH

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED]</p>

!!! danger "Site-specific: check the current Delta docs"
    Hostnames, partitions, paths, modules, and limits are set by NCSA and change over time. Check everything marked `[TEAM VERIFICATION REQUIRED]` against the [Delta documentation](https://docs.ncsa.illinois.edu/systems/delta/).

## Getting an account

| Step | Details |
|---|---|
| 1. Get added to the allocation | Ask [TEAM VERIFICATION REQUIRED]: allocation manager |
| 2. Set up your NCSA / allocation account | [TEAM VERIFICATION REQUIRED]: what we actually had to do |
| 3. Multi-factor authentication | [TEAM VERIFICATION REQUIRED]: confirm current MFA requirement in the Delta docs |

Handing access to the next team: [Access Transfer Checklist](../handoff/access-transfer.md).

## Logging in

```bash
ssh <your-username>@<delta-login-host>   # host: [TEAM VERIFICATION REQUIRED] from Delta docs
```

**Expected:** an MFA prompt (if required), then a shell on a login node.

!!! warning "Login nodes are shared"
    Don't train on login nodes. Use them only for editing files, installing environments, and submitting jobs.

## Optional: SSH config shortcut

On **your laptop**, in `~/.ssh/config`:

```text
Host delta
    HostName <delta-login-host>     # [TEAM VERIFICATION REQUIRED]
    User <your-username>
```

Then just `ssh delta`.

!!! danger "Private keys stay on your machine"
    Never commit SSH keys, `.ssh/` contents, or tokens to any repo. The repo `.gitignore` blocks common key names, but don't rely on it.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Login refused | [TEAM VERIFICATION REQUIRED] |
| MFA problems | [TEAM VERIFICATION REQUIRED] |
