import re

with open('/app/CipherVault/MainWindow.xaml', 'r') as f:
    content = f.read()

# 1. Add IconConverter reference to Window.Resources
converter_ref = '''        <local:Converters.IconConverter x:Key="IconConverter"/>
        <!-- Colors -->'''
content = content.replace('        <!-- Colors -->', converter_ref)

# 2. Update Sidebar navigation
nav_search = '''                <!-- Navigation -->
                <StackPanel Grid.Row="1">
                    <RadioButton Content="Vault" IsChecked="True" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Favorites" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Security Audit" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Settings" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                </StackPanel>'''

nav_replace = '''                <!-- Navigation -->
                <StackPanel Grid.Row="1">
                    <RadioButton IsChecked="True" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav">
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="&#xE8F1;" FontFamily="Segoe MDL2 Assets" VerticalAlignment="Center" Margin="0,0,12,0"/>
                            <TextBlock Text="Vault" VerticalAlignment="Center"/>
                        </StackPanel>
                    </RadioButton>
                    <RadioButton Style="{StaticResource SidebarMenuBtn}" GroupName="Nav">
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="&#xE728;" FontFamily="Segoe MDL2 Assets" VerticalAlignment="Center" Margin="0,0,12,0"/>
                            <TextBlock Text="Favorites" VerticalAlignment="Center"/>
                        </StackPanel>
                    </RadioButton>
                    <RadioButton Style="{StaticResource SidebarMenuBtn}" GroupName="Nav">
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="&#xE81C;" FontFamily="Segoe MDL2 Assets" VerticalAlignment="Center" Margin="0,0,12,0"/>
                            <TextBlock Text="Security Audit" VerticalAlignment="Center"/>
                        </StackPanel>
                    </RadioButton>
                    <RadioButton Style="{StaticResource SidebarMenuBtn}" GroupName="Nav">
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="&#xE713;" FontFamily="Segoe MDL2 Assets" VerticalAlignment="Center" Margin="0,0,12,0"/>
                            <TextBlock Text="Settings" VerticalAlignment="Center"/>
                        </StackPanel>
                    </RadioButton>
                </StackPanel>'''
content = content.replace(nav_search, nav_replace)

# 3. Update Search Box
search_box_search = '''                        <!-- Search Box -->
                        <Border Background="#F1F5F9" CornerRadius="16" Height="32" Padding="12,0" Margin="0,0,16,0" Width="200">
                            <Grid>
                                <TextBlock Text="Search vault items..." Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="24,0,0,0"/>
                                <TextBox Background="Transparent" BorderThickness="0" VerticalAlignment="Center" Text="{Binding SearchText, UpdateSourceTrigger=PropertyChanged}" Padding="24,0,0,0"/>
                            </Grid>
                        </Border>'''

search_box_replace = '''                        <!-- Search Box -->
                        <Border Background="#F1F5F9" CornerRadius="16" Height="32" Padding="12,0" Margin="0,0,16,0" Width="200">
                            <Grid>
                                <TextBlock Text="&#xE721;" FontFamily="Segoe MDL2 Assets" Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" Margin="0,0,8,0" HorizontalAlignment="Left"/>
                                <TextBlock Text="Search vault items..." Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="24,0,0,0">
                                    <TextBlock.Style>
                                        <Style TargetType="TextBlock">
                                            <Setter Property="Visibility" Value="Visible"/>
                                            <Style.Triggers>
                                                <DataTrigger Binding="{Binding ElementName=SearchTextBox, Path=Text.Length, FallbackValue=0}" Value="0">
                                                    <Setter Property="Visibility" Value="Visible"/>
                                                </DataTrigger>
                                                <DataTrigger Binding="{Binding ElementName=SearchTextBox, Path=Text.IsEmpty}" Value="False">
                                                    <Setter Property="Visibility" Value="Hidden"/>
                                                </DataTrigger>
                                            </Style.Triggers>
                                        </Style>
                                    </TextBlock.Style>
                                </TextBlock>
                                <TextBox x:Name="SearchTextBox" Background="Transparent" BorderThickness="0" VerticalAlignment="Center" Text="{Binding SearchText, UpdateSourceTrigger=PropertyChanged}" Padding="24,0,0,0"/>
                            </Grid>
                        </Border>'''
content = content.replace(search_box_search, search_box_replace)

# 4. Update Header Utils
header_utils_search = '''                        <!-- Header Utils -->
                        <Button Content="🔄" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="❓" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="👤" Style="{StaticResource ActionBtn}" Margin="0,0,16,0"/>'''

header_utils_replace = '''                        <!-- Header Utils -->
                        <Button Content="&#xE895;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="&#xE897;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="&#xE77B;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" Margin="0,0,16,0"/>'''
content = content.replace(header_utils_search, header_utils_replace)

# 5. Update Form Fields (Username, Password, URL)
username_search = '''                                <!-- Username Field -->
                                <StackPanel Margin="0,0,0,20">
                                    <TextBlock Text="USERNAME / EMAIL" Style="{StaticResource LabelText}" Margin="0,0,0,8"/>
                                    <Grid>
                                        <TextBox Text="{Binding SelectedVaultItem.Username}"  IsReadOnly="True"/>
                                        <Button Content="Copy" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.Username}"/>
                                    </Grid>
                                </StackPanel>'''

username_replace = '''                                <!-- Username Field -->
                                <StackPanel Margin="0,0,0,20">
                                    <TextBlock Text="USERNAME / EMAIL" Style="{StaticResource LabelText}" Margin="0,0,0,8"/>
                                    <Grid>
                                        <TextBox Text="{Binding SelectedVaultItem.Username}" Style="{StaticResource MonoInput}" Padding="12,10,70,10" IsReadOnly="True"/>
                                        <Button Content="&#xE8C8;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.Username}"/>
                                    </Grid>
                                </StackPanel>'''
content = content.replace(username_search, username_replace)

password_search = '''                                <!-- Password Field -->
                                <StackPanel Margin="0,0,0,8">
                                    <TextBlock Text="PASSWORD" Style="{StaticResource LabelText}" Margin="0,0,0,8"/>
                                    <Grid>
                                        <TextBox  IsReadOnly="True" x:Name="PasswordBox">
                                            <TextBox.Style>
                                                <Style TargetType="TextBox" BasedOn="{StaticResource MonoInput}">
                                                    <Setter Property="Text" Value="••••••••••••••••••••"/>
                                                    <Style.Triggers>
                                                        <DataTrigger Binding="{Binding IsPasswordVisible}" Value="True">
                                                            <Setter Property="Text" Value="{Binding SelectedVaultItem.EncryptedPassword}"/>
                                                        </DataTrigger>
                                                    </Style.Triggers>
                                                </Style>
                                            </TextBox.Style>
                                        </TextBox>
                                        <StackPanel Orientation="Horizontal" HorizontalAlignment="Right" Margin="4">
                                            <Button Content="Show" Style="{StaticResource ActionBtn}" Command="{Binding TogglePasswordVisibilityCommand}"/>
                                            <Button Content="Copy" Style="{StaticResource ActionBtn}" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.EncryptedPassword}"/>
                                        </StackPanel>
                                    </Grid>
                                </StackPanel>'''

password_replace = '''                                <!-- Password Field -->
                                <StackPanel Margin="0,0,0,8">
                                    <TextBlock Text="PASSWORD" Style="{StaticResource LabelText}" Margin="0,0,0,8"/>
                                    <Grid>
                                        <TextBox IsReadOnly="True" x:Name="PasswordBox" Padding="12,10,120,10">
                                            <TextBox.Style>
                                                <Style TargetType="TextBox" BasedOn="{StaticResource MonoInput}">
                                                    <Setter Property="Text" Value="••••••••••••••••••••"/>
                                                    <Style.Triggers>
                                                        <DataTrigger Binding="{Binding IsPasswordVisible}" Value="True">
                                                            <Setter Property="Text" Value="{Binding SelectedVaultItem.EncryptedPassword}"/>
                                                        </DataTrigger>
                                                    </Style.Triggers>
                                                </Style>
                                            </TextBox.Style>
                                        </TextBox>
                                        <StackPanel Orientation="Horizontal" HorizontalAlignment="Right" Margin="4">
                                            <Button Content="&#xE890;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" Command="{Binding TogglePasswordVisibilityCommand}"/>
                                            <Button Content="&#xE8C8;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.EncryptedPassword}"/>
                                        </StackPanel>
                                    </Grid>
                                </StackPanel>'''
content = content.replace(password_search, password_replace)

url_search = '''                                <!-- Website URL Field -->
                                <StackPanel Margin="0,0,0,24">
                                    <TextBlock Text="WEBSITE / URL" Style="{StaticResource LabelText}" Margin="0,0,0,8"/>
                                    <Grid>
                                        <TextBox Text="{Binding SelectedVaultItem.Url}"  IsReadOnly="True"/>
                                        <Button Content="Open" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding LaunchExternalUrlCommand}" CommandParameter="{Binding SelectedVaultItem.Url}"/>
                                    </Grid>
                                </StackPanel>'''

url_replace = '''                                <!-- Website URL Field -->
                                <StackPanel Margin="0,0,0,24">
                                    <TextBlock Text="WEBSITE / URL" Style="{StaticResource LabelText}" Margin="0,0,0,8"/>
                                    <Grid>
                                        <TextBox Text="{Binding SelectedVaultItem.Url}" Style="{StaticResource MonoInput}" Padding="12,10,70,10" IsReadOnly="True"/>
                                        <Button Content="&#xE8A7;" FontFamily="Segoe MDL2 Assets" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding LaunchExternalUrlCommand}" CommandParameter="{Binding SelectedVaultItem.Url}"/>
                                    </Grid>
                                </StackPanel>'''
content = content.replace(url_search, url_replace)

# 6. Update Security Insights icons
insights_search = '''                                <Grid Margin="0,0,0,12">
                                    <Grid.ColumnDefinitions>
                                        <ColumnDefinition Width="Auto"/>
                                        <ColumnDefinition Width="*"/>
                                    </Grid.ColumnDefinitions>
                                    <TextBlock Text="🛡" FontSize="16" Margin="0,0,12,0"/>
                                    <StackPanel Grid.Column="1">
                                        <TextBlock Text="MFA Enabled" Style="{StaticResource BaseText}" FontWeight="SemiBold"/>
                                        <TextBlock Text="{Binding SelectedVaultItem.MfaStatus}" Style="{StaticResource LabelText}" FontWeight="Normal"/>
                                    </StackPanel>
                                </Grid>

                                <Grid Margin="0,0,0,12">
                                    <Grid.ColumnDefinitions>
                                        <ColumnDefinition Width="Auto"/>
                                        <ColumnDefinition Width="*"/>
                                    </Grid.ColumnDefinitions>
                                    <TextBlock Text="📅" FontSize="16" Margin="0,0,12,0"/>
                                    <StackPanel Grid.Column="1">
                                        <TextBlock Text="Last Rotated" Style="{StaticResource BaseText}" FontWeight="SemiBold"/>
                                        <TextBlock Text="12 days ago" Style="{StaticResource LabelText}" FontWeight="Normal"/>
                                    </StackPanel>
                                </Grid>

                                <Grid>
                                    <Grid.ColumnDefinitions>
                                        <ColumnDefinition Width="Auto"/>
                                        <ColumnDefinition Width="*"/>
                                    </Grid.ColumnDefinitions>
                                    <TextBlock Text="✓" FontSize="16" Margin="0,0,12,0" Foreground="{StaticResource PrimaryBrush}"/>
                                    <StackPanel Grid.Column="1">
                                        <TextBlock Text="Breach Status" Style="{StaticResource BaseText}" FontWeight="SemiBold"/>
                                        <TextBlock Text="{Binding SelectedVaultItem.BreachStatus}" Style="{StaticResource LabelText}" FontWeight="Normal"/>
                                    </StackPanel>
                                </Grid>'''

insights_replace = '''                                <Grid Margin="0,0,0,12">
                                    <Grid.ColumnDefinitions>
                                        <ColumnDefinition Width="Auto"/>
                                        <ColumnDefinition Width="*"/>
                                    </Grid.ColumnDefinitions>
                                    <TextBlock Text="&#xEA18;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0"/>
                                    <StackPanel Grid.Column="1">
                                        <TextBlock Text="MFA Enabled" Style="{StaticResource BaseText}" FontWeight="SemiBold"/>
                                        <TextBlock Text="{Binding SelectedVaultItem.MfaStatus}" Style="{StaticResource LabelText}" FontWeight="Normal"/>
                                    </StackPanel>
                                </Grid>

                                <Grid Margin="0,0,0,12">
                                    <Grid.ColumnDefinitions>
                                        <ColumnDefinition Width="Auto"/>
                                        <ColumnDefinition Width="*"/>
                                    </Grid.ColumnDefinitions>
                                    <TextBlock Text="&#xE787;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0"/>
                                    <StackPanel Grid.Column="1">
                                        <TextBlock Text="Last Rotated" Style="{StaticResource BaseText}" FontWeight="SemiBold"/>
                                        <TextBlock Text="12 days ago" Style="{StaticResource LabelText}" FontWeight="Normal"/>
                                    </StackPanel>
                                </Grid>

                                <Grid>
                                    <Grid.ColumnDefinitions>
                                        <ColumnDefinition Width="Auto"/>
                                        <ColumnDefinition Width="*"/>
                                    </Grid.ColumnDefinitions>
                                    <TextBlock Text="&#xE73E;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0" Foreground="{StaticResource PrimaryBrush}"/>
                                    <StackPanel Grid.Column="1">
                                        <TextBlock Text="Breach Status" Style="{StaticResource BaseText}" FontWeight="SemiBold"/>
                                        <TextBlock Text="{Binding SelectedVaultItem.BreachStatus}" Style="{StaticResource LabelText}" FontWeight="Normal"/>
                                    </StackPanel>
                                </Grid>'''
content = content.replace(insights_search, insights_replace)

# 7. Update Audit Logs icon binding
audit_log_search = '''                                                <!-- Icon Badge -->
                                                <Border Width="24" Height="24" CornerRadius="12" Background="#F1F5F9" Margin="0,0,12,0" VerticalAlignment="Top">
                                                    <TextBlock Text="•" VerticalAlignment="Center" HorizontalAlignment="Center" Foreground="{StaticResource TextMutedBrush}"/>
                                                </Border>'''

audit_log_replace = '''                                                <!-- Icon Badge -->
                                                <Border Width="24" Height="24" CornerRadius="12" Background="#F1F5F9" Margin="0,0,12,0" VerticalAlignment="Top">
                                                    <TextBlock Text="{Binding IconType, Converter={StaticResource IconConverter}}" FontFamily="Segoe MDL2 Assets" VerticalAlignment="Center" HorizontalAlignment="Center" Foreground="{StaticResource TextMutedBrush}"/>
                                                </Border>'''
content = content.replace(audit_log_search, audit_log_replace)

# 8. Add xmlns:localConverters
content = content.replace('xmlns:viewmodels="clr-namespace:CipherVault.ViewModels"', 'xmlns:viewmodels="clr-namespace:CipherVault.ViewModels"\n        xmlns:localConverters="clr-namespace:CipherVault.Converters"')
content = content.replace('<local:Converters.IconConverter x:Key="IconConverter"/>', '<localConverters:IconConverter x:Key="IconConverter"/>')


# 9. Add Toast Notification
toast_search = '''        </Grid>
    </Grid>
</Window>'''

toast_replace = '''        </Grid>

        <!-- Toast Notification -->
        <Border Background="{StaticResource TextPrimaryBrush}" CornerRadius="8" Padding="16,12"
                HorizontalAlignment="Center" VerticalAlignment="Bottom" Margin="0,0,0,32"
                Panel.ZIndex="100" Grid.ColumnSpan="2">
            <Border.Style>
                <Style TargetType="Border">
                    <Setter Property="Visibility" Value="Collapsed"/>
                    <Style.Triggers>
                        <DataTrigger Binding="{Binding IsToastVisible}" Value="True">
                            <Setter Property="Visibility" Value="Visible"/>
                        </DataTrigger>
                    </Style.Triggers>
                </Style>
            </Border.Style>
            <StackPanel Orientation="Horizontal">
                <TextBlock Text="&#xE73E;" FontFamily="Segoe MDL2 Assets" Foreground="{StaticResource PrimaryBrush}" VerticalAlignment="Center" Margin="0,0,8,0"/>
                <TextBlock Text="{Binding ToastMessage}" Foreground="White" FontWeight="Medium" VerticalAlignment="Center"/>
            </StackPanel>
        </Border>
    </Grid>
</Window>'''
content = content.replace(toast_search, toast_replace)


with open('/app/CipherVault/MainWindow.xaml', 'w') as f:
    f.write(content)
