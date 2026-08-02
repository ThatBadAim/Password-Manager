import re

with open("CipherVault/MainWindow.xaml", "r") as f:
    content = f.read()

# Fix the password masking
password_box_original = """                                        <TextBox  IsReadOnly="True" x:Name="PasswordBox">
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
                                        </TextBox>"""

# The password visibility works by swapping the string, this is correct for TextBox as provided in the skeleton
# But wait, looking at the XAML above, it actually DOES toggle between ••• and plain text using DataTrigger.
# Is the code reviewer mistaken? Let me double check the XAML from MainWindow.xaml
