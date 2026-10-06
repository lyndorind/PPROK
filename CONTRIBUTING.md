# Contributing 

Thank you for your interest in contributing to PPROK.

Contributions may include bug fixes, new features, documentation improvements, bug reports, feature requests, and Pull Request reviews.

Before contributing, please check existing Issues and Pull Requests to avoid duplicate work.

## Development Workflow

PPROK follows a GitHub Flow-style development workflow.

The `main` branch is the primary protected branch. Changes should not be made directly in `main`.

For each change:

1. Create or select an Issue describing the requested change.
2. Create a separate branch from the current `main` branch.
3. Implement the required changes.
4. Run local checks.
5. Commit and push the changes.
6. Create a Pull Request to `main`.
7. Wait for the required GitHub Actions checks.
8. Request a review from another contributor.
9. Resolve review comments if necessary.
10. Merge the Pull Request using **Squash and merge**.

## Branches

Use short and descriptive branch names.

Recommended formats:
- `feature/<description>`
- `fix/<description>`
- `docs/<description>`
- `issue-<number>-<description>`

Examples:
- `feature/add-version-endpoint`
- `fix/input-validation`
- `docs/update-readme`
- `issue-4-version-endpoint`

One branch should normally contain one logical change.

## Development Setup

Install project dependencies with `uv sync`.

Before creating a Pull Request, run `uv run ruff check .`.

Make sure all local checks complete successfully.

## Issues

For non-trivial changes, create an Issue before implementation.

An Issue should include:
- a clear description of the problem or requested change;
- the proposed solution;
- the expected result;
- acceptance criteria when applicable.

## Pull Requests

Pull Requests should target the `main` branch.

A Pull Request should contain:
- a clear title;
- a short description of the changes;
- a reference to the related Issue;
- information about completed checks.

If the Pull Request resolves an Issue, use `Closes #<issue-number>`.

All required GitHub Actions checks must pass before merging.

## Code Review

Every Pull Request should be reviewed by another contributor.

A reviewer may:
- leave comments;
- approve the changes;
- request changes.

At least one approving review is required before merging into `main`.

## Merge Strategy

PPROK uses **Squash and merge**.

A Pull Request can be merged only when:
- all required checks have passed;
- the required review has been received;
- requested changes have been resolved.

## Code of Conduct

All contributors are expected to follow the project [Code of Conduct](CODE_OF_CONDUCT.md).

Please communicate respectfully and provide constructive feedback when working with Issues, Pull Requests, and Code Reviews.
