# Goal
Resolve the assigned configuration PR #3 and prepare a separate same-org integration for fork PR #2, preserving all original tips and native behavior.

# State
Fresh master dd2efbd802ec66ad8481a13335d2baed71729e96. PR #3 published/local review tip 67c3a10155a83d9fe8a3c4eccb1dcf7fef724ed5 is separately archived under archive/task6-keyboard-handler-pr3-local and archive/task6-keyboard-handler-pr3-published; canonical tip has its own archive. Canonical untracked CLAUDE.md and kw.zip and original review worktrees are untouched. This isolated branch rebases only the historical seven-line Dependabot migration onto fresh master with --no-update-refs.

# Decisions and why
The PR changes update configuration, not keyboard runtime behavior. Its relevant safe gate validates the actual Dependabot schema, builds both distributions using setup.py/find_packages, and checks distribution metadata with Twine. No package/platform handler is imported, no keys are captured and no new behavioral tests are invented. One Python 3.12/Linux runner is gate coverage, not a support-policy declaration. Pinned current official actions use read-only permissions, no persisted credentials, timeout and superseded-run concurrency; an Actions-only maintenance entry is added to the original pip schedule. Existing release/support behavior is unchanged.

# Surprises
Fork PR #2 targets an old 0.52 setup.py while master is 0.53; merging its stale file wholesale would lose current metadata/native fixes. Its original external-author branch must never be pushed. That slice remains separate and serialized after this configuration prerequisite.

# Next step
actionlint 1.7.12 passed; offline zizmor 1.31.1 reported no findings (one default suppression). Return complete committed local diff/head for coordinator review before publication. No full local CI runs, model calls, settings changes, release or merge actions. Hosted schema/build/metadata execution remains pending publication.
