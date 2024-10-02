To connect your PC to your GitHub account using an SSH key, follow these steps:

### 1. Generate a new SSH key (if you don't have one)
First, check if you already have an SSH key by running the following command in your terminal:

```bash
ls -al ~/.ssh
```

If you see `id_rsa` or `id_ed25519`, you already have an SSH key. If not, generate one using these steps:

- Open your terminal and type the following command to generate a new SSH key:

    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

    Make sure to replace `"your_email@example.com"` with the email associated with your GitHub account.

- You will be prompted to choose a location to save the key. Press `Enter` to accept the default location.

- When asked for a passphrase, you can either enter one (for added security) or leave it empty by pressing `Enter`.

### 2. Add your SSH key to the SSH agent
Once your SSH key is generated, you need to add it to the SSH agent so it can manage your key.

- Start the SSH agent:

    ```bash
    eval "$(ssh-agent -s)"
    ```

- Add your SSH private key to the agent:

    ```bash
    ssh-add ~/.ssh/id_rsa
    ```

    If you used a different name for the key file, replace `id_rsa` with your custom name.

### 3. Add your SSH key to your GitHub account
Now, you need to add the SSH public key to your GitHub account.

- Copy the SSH key to your clipboard:

    ```bash
    cat ~/.ssh/id_rsa.pub
    ```

    Or, if you used `pbcopy` (on macOS), you can use:

    ```bash
    pbcopy < ~/.ssh/id_rsa.pub
    ```

- Log in to your GitHub account and go to **Settings**.
- In the left sidebar, click **SSH and GPG keys**.
- Click **New SSH key**.
- Paste your SSH key into the "Key" field and give it a title (e.g., "My PC").
- Click **Add SSH key**.

### 4. Test your SSH connection
Now that your SSH key is added, test your connection to GitHub by running the following command in your terminal:

```bash
ssh -T git@github.com
```

If everything is set up correctly, you should see a message like this:

```bash
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

This confirms that your PC is connected to GitHub via SSH.

### 5. Clone repositories using SSH
Now that your SSH key is connected, you can clone repositories using the SSH URL. For example:

```bash
git clone git@github.com:username/repository.git
```

That's it! You are now connected to GitHub via SSH.
