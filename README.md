# Merge Conflict Exercise: TechMart Checkout

## Learning objectives

By the end of this exercise your group will have:

- Practiced **trunk-based development**: short-lived feature branches, merged back into `main` frequently, instead of long-lived branches.
- Practiced granting GitHub repo access to teammates and collaborating on shared branches with pull requests.
- Created and **resolved a real merge conflict** because two people genuinely had to edit the same lines of code to implement two different features.

## Group formation

Work in groups of **2** (groups of **3** only if needed to cover everyone,
e.g. an odd number of students).

Within your group, agree on one **Repo Owner**. This person forks the repo
and grants their teammates push access to that one fork. There is only one
repo per group, not one per person. **The Repo Owner's fork is the one link
the whole group submits on Blackboard**, and its git history is what gets
graded, so it must contain every feature branch and the merge-conflict
resolution commit. Keep the fork **public** (the default when forking a
public repo) so the professor can open and grade it without needing
collaborator access.

## The setup

`store.py` has one function, `calculate_total`, with a single TODO comment.
Below are the features your group needs to add. Every feature is implemented
at that same TODO line on purpose. That's what guarantees a real conflict
when you merge two of them together.

## Feature assignments

Your group must implement **all** of the features below (2-person groups
skip Feature C; 3-person groups implement all three). Each teammate takes
exactly one feature. Don't look at each other's code while implementing,
since part of the exercise is not knowing exactly what the other person changed
until you merge. Figure out how to write the code yourself; it's a small,
straightforward change.

- **Feature A: Loyalty discount**. Orders with a subtotal over $50 get a
  10% discount.
- **Feature B: Sales tax**. Add an 8% sales tax to every order.
- **Feature C: Flat shipping fee** (3-person groups only). Add a flat $5
  shipping fee to every order.

Once you're done, sanity-check your own feature in isolation (see "Using uv"
below for how to run a single test), using whichever test name matches your
feature: `test_discount_feature_alone`, `test_tax_feature_alone`, or
`test_shipping_feature_alone`.

### Combining the features (for whoever resolves the conflict)

The business rule, once all features exist together, is that pricing rules
are applied **in order: A, then B, then C** (discount, then tax, then
shipping). When you resolve the merge conflict, don't just keep both hunks
side by side. Rewrite the block so the rules are applied in that order.
Verify with the `test_all_features_combined` test.

## Using uv

This repo uses [uv](https://docs.astral.sh/uv/) to manage the Python
environment. Install uv once per machine (see uv's docs), then from inside
the repo:

```bash
uv venv                              # create a local virtual environment (.venv)
uv pip install -r requirements.txt   # install pytest into it
```

From then on, run any Python command through `uv run` so it uses that
environment automatically, e.g.:

```bash
uv run pytest test_store.py
uv run pytest test_store.py::test_tax_feature_alone   # run a single test
```

## Continuous integration

This repo includes a GitHub Actions workflow (`.github/workflows/tests.yml`)
that runs the full test suite automatically on every pull request. You'll
see the check's status at the bottom of each PR on GitHub. It's normal for
it to fail on an individual feature branch's PR, since only your one
feature is implemented at that point. It should be green once a PR merges
all of a group's features together and the conflict is resolved correctly.

## Step-by-step instructions

### 1. Repo Owner forks the repo

The Repo Owner forks this repository to their own GitHub account. Nobody
else forks it. Everyone else will work directly in this one fork.

### 2. Repo Owner grants the team access

On GitHub, in the forked repo: **Settings → Collaborators and teams**
(under "Access" in the left sidebar) → **Add people** → enter each
teammate's GitHub username or email → send the invite. Each teammate gets a
notification/email and must **accept the invitation** before they can push
to the repo.

### 3. Everyone clones the same repo

Everyone, including the Repo Owner, clones the **same** URL: the Repo
Owner's fork.

```bash
git clone <repo-owner-fork-url>
cd sdd-git-merge-conflict-exercise
```

### 4. Pick your features

As a group, agree on who implements which feature: A and B for two-person
groups, or A, B, and C for three-person groups. See the "Feature
assignments" section above.

### 5. Work on a short-lived feature branch

This is the trunk-based development part: **never** commit your feature
directly to `main`, and don't let the branch live for more than this one
session. Everyone creates their own branch:

```bash
git checkout -b feature/<your-feature-name>   # e.g. feature/tax
```

Implement your assigned feature in `store.py`, then commit:

```bash
git add store.py
git commit -m "Add <feature name>"
```

Sanity-check your own feature in isolation:

```bash
uv run pytest test_store.py::test_<feature>_feature_alone
```

### 6. Push your branch and open a pull request

Since you now have push access to the shared repo, push your branch there
directly:

```bash
git push origin feature/<your-feature-name>
```

Then, on GitHub, open a **Pull Request** from your branch into `main`.

### 7. Merge the first pull request

Whoever's feature is ready first merges their PR into `main` on GitHub (a
regular, conflict-free merge, since nothing else has touched `main` yet).
Everyone should then run `git checkout main && git pull` locally to pick up
that change.

### 8. Merge the second pull request and resolve the conflict

The second PR will now conflict with `main`, since it touches the same
lines the first PR already changed. Don't resolve conflicts in the GitHub
web UI. Resolve them locally so you get the real experience. Whoever is
merging (can be the Repo Owner, or the PR author) runs:

```bash
git checkout main
git pull
git merge feature/<second-feature-name>
```

Git will report a conflict in `store.py`. Open it, look at the
`<<<<<<<` / `=======` / `>>>>>>>` markers, and rewrite the block so **both**
features are applied correctly together (see "Combining the features"
above for the required order). Don't just keep both hunks stacked in the
wrong order and call it done.

Once it looks right:

```bash
git add store.py
git commit
uv run pytest test_store.py::test_all_features_combined
git push origin main
```

Pushing to `main` will automatically close/merge the corresponding pull
request on GitHub.

### 9. Three-person groups: repeat for the third feature

If your group has three people, repeat steps 6 to 8 for the third feature
branch. Merging it will very likely conflict again, since it's landing on
top of an already-modified function. Resolve it the same way, following the
full A/B/C order above.

### 10. Verify and submit

On `main`, all tests should now pass:

```bash
uv run pytest test_store.py
```

`test_all_features_combined` passing confirms every teammate's feature
survived the conflict resolution intact.

**Every student submits the Repo Owner's fork URL on Blackboard, individually.**
It's the same link for the whole group, but each person turns it in
themselves so everyone's participation is recorded. Its git history should
show: each feature branch's commit(s), and a merge commit where the conflict
in `store.py` was resolved.

## Important

- The repo's history should show genuinely separate feature branches from
  different contributors (check the commit authors). Do not delete the branches after merging into `main`.
- Make sure there is an actual merge commit with a real conflict resolution, do not squash or rebase the changes.
- `test_all_features_combined` passes on the final `main`.
- No long-lived branches: feature branches should be short, and merged back
  promptly, per trunk-based development.
