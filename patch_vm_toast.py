with open("CipherVault/ViewModels/MainViewModel.cs", "r") as f:
    content = f.read()

# Replace async void ShowToast with async Task and use a cancellation token for better toast overlapping
import re
old_toast = """        private async void ShowToast(string message)
        {
            ToastMessage = message;
            IsToastVisible = true;
            await Task.Delay(3000);
            IsToastVisible = false;
        }"""

new_toast = """        private System.Threading.CancellationTokenSource? _toastCts;

        private async Task ShowToastAsync(string message)
        {
            _toastCts?.Cancel();
            _toastCts = new System.Threading.CancellationTokenSource();
            var token = _toastCts.Token;

            ToastMessage = message;
            IsToastVisible = true;

            try
            {
                await Task.Delay(3000, token);
                if (!token.IsCancellationRequested)
                {
                    IsToastVisible = false;
                }
            }
            catch (TaskCanceledException) { }
        }"""

content = content.replace(old_toast, new_toast)

# Update CopyToClipboard to use the async method
old_copy = """        [RelayCommand]
        private void CopyToClipboard(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                ShowToast("Copied to clipboard!");
            }
        }"""

new_copy = """        [RelayCommand]
        private async Task CopyToClipboardAsync(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                await ShowToastAsync("Copied to clipboard!");
            }
        }"""

content = content.replace(old_copy, new_copy)

with open("CipherVault/ViewModels/MainViewModel.cs", "w") as f:
    f.write(content)
