import re

with open("CipherVault/MainWindow.xaml", "r") as f:
    content = f.read()

# 1. Update Sidebar Navigation
sidebar_nav_original = """                <!-- Navigation -->
                <StackPanel Grid.Row="1">
                    <RadioButton Content="Vault" IsChecked="True" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Favorites" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Security Audit" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Settings" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                </StackPanel>"""

sidebar_nav_new = """                <!-- Navigation -->
                <StackPanel Grid.Row="1">
                    <RadioButton IsChecked="True" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav">
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="&#xE8F1;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0" VerticalAlignment="Center"/>
                            <TextBlock Text="Vault" VerticalAlignment="Center"/>
                        </StackPanel>
                    </RadioButton>
                    <RadioButton Style="{StaticResource SidebarMenuBtn}" GroupName="Nav">
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="&#xE734;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0" VerticalAlignment="Center"/>
                            <TextBlock Text="Favorites" VerticalAlignment="Center"/>
                        </StackPanel>
                    </RadioButton>
                    <RadioButton Style="{StaticResource SidebarMenuBtn}" GroupName="Nav">
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="&#xE773;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0" VerticalAlignment="Center"/>
                            <TextBlock Text="Security Audit" VerticalAlignment="Center"/>
                        </StackPanel>
                    </RadioButton>
                    <RadioButton Style="{StaticResource SidebarMenuBtn}" GroupName="Nav">
                        <StackPanel Orientation="Horizontal">
                            <TextBlock Text="&#xE713;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0" VerticalAlignment="Center"/>
                            <TextBlock Text="Settings" VerticalAlignment="Center"/>
                        </StackPanel>
                    </RadioButton>
                </StackPanel>"""

content = content.replace(sidebar_nav_original, sidebar_nav_new)

# 2. Add Toast Notification overlay
toast_overlay = """            </ScrollViewer>
        </Grid>

        <!-- Toast Notification Overlay -->
        <Border Grid.Column="1" HorizontalAlignment="Right" VerticalAlignment="Bottom" Margin="24"
                Background="#1E293B" CornerRadius="8" Padding="16,12"
                Visibility="{Binding IsToastVisible, Converter={StaticResource BooleanToVisibilityConverter}}">
            <TextBlock Text="{Binding ToastMessage}" Foreground="White" FontSize="14" FontWeight="Medium"/>
        </Border>

    </Grid>
</Window>"""

content = content.replace("            </ScrollViewer>\n        </Grid>\n    </Grid>\n</Window>", toast_overlay)

# Make sure BooleanToVisibilityConverter is in resources
resource_end = """    </Window.Resources>"""
resource_with_converter = """        <BooleanToVisibilityConverter x:Key="BooleanToVisibilityConverter"/>
    </Window.Resources>"""

content = content.replace(resource_end, resource_with_converter)

with open("CipherVault/MainWindow.xaml", "w") as f:
    f.write(content)
