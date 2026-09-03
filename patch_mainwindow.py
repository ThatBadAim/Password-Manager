import re

with open("CipherVault/MainWindow.xaml", "r", encoding="utf-8") as f:
    content = f.read()

# Add IconConverter namespace and resource
ns_pattern = r'xmlns:viewmodels="clr-namespace:CipherVault.ViewModels"'
content = content.replace(ns_pattern, ns_pattern + '\n        xmlns:converters="clr-namespace:CipherVault.Converters"')

res_pattern = r'<Window.Resources>'
res_replacement = r'''<Window.Resources>
        <converters:IconConverter x:Key="IconConverter"/>

        <!-- Boolean to Visibility Converter for Toast -->
        <BooleanToVisibilityConverter x:Key="BoolToVis"/>'''
content = content.replace(res_pattern, res_replacement)

# Update MonoInput padding
mono_pattern = r'<Setter Property="Padding" Value="12,10"/>'
mono_replacement = r'<Setter Property="Padding" Value="12,10,70,10"/>'
content = content.replace(mono_pattern, mono_replacement)

# Update Toast Notification
# We'll add the toast notification at the end of the main grid before closing the Window
toast_xaml = r'''
        <!-- Toast Notification -->
        <Border HorizontalAlignment="Center" VerticalAlignment="Bottom" Margin="0,0,0,32"
                Background="{StaticResource TextPrimaryBrush}" CornerRadius="6"
                Padding="16,12" Panel.ZIndex="100"
                Visibility="{Binding IsToastVisible, Converter={StaticResource BoolToVis}}">
            <StackPanel Orientation="Horizontal">
                <TextBlock Text="&#xE73E;" FontFamily="Segoe MDL2 Assets" Foreground="White" Margin="0,0,8,0" VerticalAlignment="Center"/>
                <TextBlock Text="{Binding ToastMessage}" Foreground="White" VerticalAlignment="Center" FontWeight="Medium" FontSize="13"/>
            </StackPanel>
        </Border>
    </Grid>
</Window>'''
content = content.replace('    </Grid>\n</Window>', toast_xaml)

# Update simple emojis to Segoe MDL2 Assets
content = content.replace('<Button Content="🔄" Style="{StaticResource ActionBtn}"', '<Button Content="&#xE72C;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}"')
content = content.replace('<Button Content="❓" Style="{StaticResource ActionBtn}"', '<Button Content="&#xE897;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}"')
content = content.replace('<Button Content="👤" Style="{StaticResource ActionBtn}"', '<Button Content="&#xE77B;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}"')
content = content.replace('<TextBlock Text="🛡" FontSize="16"', '<TextBlock Text="&#xEA18;" FontFamily="Segoe MDL2 Assets" FontSize="16"')
content = content.replace('<TextBlock Text="📅" FontSize="16"', '<TextBlock Text="&#xE787;" FontFamily="Segoe MDL2 Assets" FontSize="16"')
content = content.replace('<TextBlock Text="✓" FontSize="16"', '<TextBlock Text="&#xE73E;" FontFamily="Segoe MDL2 Assets" FontSize="16"')

# Update Icon for Audit Logs
audit_pattern = r'<TextBlock Text="•" VerticalAlignment="Center" HorizontalAlignment="Center" Foreground="{StaticResource TextMutedBrush}"/>'
audit_replacement = r'<TextBlock Text="{Binding IconType, Converter={StaticResource IconConverter}}" FontFamily="Segoe MDL2 Assets" VerticalAlignment="Center" HorizontalAlignment="Center" Foreground="{StaticResource TextMutedBrush}"/>'
content = content.replace(audit_pattern, audit_replacement)

# Update action buttons in inputs to be icons instead of text, and right align correctly
# 1. Username Copy
user_copy_p = r'<Button Content="Copy" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.Username}"/>'
user_copy_r = r'<Button Content="&#xE8C8;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.Username}"/>'
content = content.replace(user_copy_p, user_copy_r)

# 2. Password Actions (Show, Copy)
pass_show_p = r'<Button Content="Show" Style="{StaticResource ActionBtn}" Command="{Binding TogglePasswordVisibilityCommand}"/>'
pass_show_r = r'''<Button Style="{StaticResource ActionBtn}" Command="{Binding TogglePasswordVisibilityCommand}">
                                                <Button.Style>
                                                    <Style TargetType="Button" BasedOn="{StaticResource ActionBtn}">
                                                        <Setter Property="Content" Value="&#xE18B;"/>
                                                        <Setter Property="FontFamily" Value="Segoe MDL2 Assets"/>
                                                        <Style.Triggers>
                                                            <DataTrigger Binding="{Binding IsPasswordVisible}" Value="True">
                                                                <Setter Property="Content" Value="&#xE890;"/>
                                                            </DataTrigger>
                                                        </Style.Triggers>
                                                    </Style>
                                                </Button.Style>
                                            </Button>'''
content = content.replace(pass_show_p, pass_show_r)

pass_copy_p = r'<Button Content="Copy" Style="{StaticResource ActionBtn}" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.EncryptedPassword}"/>'
pass_copy_r = r'<Button Content="&#xE8C8;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.EncryptedPassword}"/>'
content = content.replace(pass_copy_p, pass_copy_r)

# 3. URL Open
url_open_p = r'<Button Content="Open" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding LaunchExternalUrlCommand}" CommandParameter="{Binding SelectedVaultItem.Url}"/>'
url_open_r = r'<Button Content="&#xE8A7;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding LaunchExternalUrlCommand}" CommandParameter="{Binding SelectedVaultItem.Url}"/>'
content = content.replace(url_open_p, url_open_r)

with open("CipherVault/MainWindow.xaml", "w", encoding="utf-8") as f:
    f.write(content)
