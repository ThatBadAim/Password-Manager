import re

with open("CipherVault/MainWindow.xaml", "r") as f:
    content = f.read()

# 1. Replace emojis with Segoe MDL2 Assets for Security Insights
sec_mfa_original = """                                    <TextBlock Text="🛡" FontSize="16" Margin="0,0,12,0"/>"""
sec_mfa_new = """                                    <TextBlock Text="&#xEA18;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0"/>"""
content = content.replace(sec_mfa_original, sec_mfa_new)

sec_cal_original = """                                    <TextBlock Text="📅" FontSize="16" Margin="0,0,12,0"/>"""
sec_cal_new = """                                    <TextBlock Text="&#xE787;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0"/>"""
content = content.replace(sec_cal_original, sec_cal_new)

sec_chk_original = """                                    <TextBlock Text="✓" FontSize="16" Margin="0,0,12,0" Foreground="{StaticResource PrimaryBrush}"/>"""
sec_chk_new = """                                    <TextBlock Text="&#xE814;" FontFamily="Segoe MDL2 Assets" FontSize="16" Margin="0,0,12,0" Foreground="{StaticResource PrimaryBrush}"/>"""
content = content.replace(sec_chk_original, sec_chk_new)

# 2. Implement vertical timeline and DataTemplate for AuditLogs
history_original = """                                <ItemsControl ItemsSource="{Binding SelectedVaultItem.AuditLogs}">
                                    <ItemsControl.ItemTemplate>
                                        <DataTemplate>
                                            <Grid Margin="0,0,0,16">
                                                <Grid.ColumnDefinitions>
                                                    <ColumnDefinition Width="Auto"/>
                                                    <ColumnDefinition Width="*"/>
                                                </Grid.ColumnDefinitions>
                                                <!-- Icon Badge -->
                                                <Border Width="24" Height="24" CornerRadius="12" Background="#F1F5F9" Margin="0,0,12,0" VerticalAlignment="Top">
                                                    <TextBlock Text="•" VerticalAlignment="Center" HorizontalAlignment="Center" Foreground="{StaticResource TextMutedBrush}"/>
                                                </Border>
                                                <StackPanel Grid.Column="1">
                                                    <TextBlock Text="{Binding ActionType}" Style="{StaticResource BaseText}" FontWeight="SemiBold" FontSize="13"/>
                                                    <TextBlock Text="{Binding Timestamp, StringFormat='g'}" Style="{StaticResource LabelText}" FontWeight="Normal" FontSize="11" Margin="0,2,0,0"/>
                                                </StackPanel>
                                            </Grid>
                                        </DataTemplate>
                                    </ItemsControl.ItemTemplate>
                                </ItemsControl>"""

history_new = """                                <Grid>
                                    <Rectangle Width="2" Fill="#E2E8F0" HorizontalAlignment="Left" Margin="11,12,0,12" VerticalAlignment="Stretch" />
                                    <ItemsControl ItemsSource="{Binding SelectedVaultItem.AuditLogs}">
                                        <ItemsControl.ItemTemplate>
                                            <DataTemplate>
                                                <Grid Margin="0,0,0,16">
                                                    <Grid.ColumnDefinitions>
                                                        <ColumnDefinition Width="Auto"/>
                                                        <ColumnDefinition Width="*"/>
                                                    </Grid.ColumnDefinitions>
                                                    <!-- Icon Badge -->
                                                    <Border Width="24" Height="24" CornerRadius="12" Margin="0,0,12,0" VerticalAlignment="Top">
                                                        <Border.Style>
                                                            <Style TargetType="Border">
                                                                <Setter Property="Background" Value="#F1F5F9"/>
                                                                <Style.Triggers>
                                                                    <DataTrigger Binding="{Binding IconType}" Value="Pencil">
                                                                        <Setter Property="Background" Value="#E0E7FF"/>
                                                                    </DataTrigger>
                                                                    <DataTrigger Binding="{Binding IconType}" Value="Eye">
                                                                        <Setter Property="Background" Value="#F1F5F9"/>
                                                                    </DataTrigger>
                                                                    <DataTrigger Binding="{Binding IconType}" Value="Copy">
                                                                        <Setter Property="Background" Value="#F1F5F9"/>
                                                                    </DataTrigger>
                                                                    <DataTrigger Binding="{Binding IconType}" Value="Plus">
                                                                        <Setter Property="Background" Value="#F1F5F9"/>
                                                                    </DataTrigger>
                                                                </Style.Triggers>
                                                            </Style>
                                                        </Border.Style>

                                                        <TextBlock FontFamily="Segoe MDL2 Assets" FontSize="12" VerticalAlignment="Center" HorizontalAlignment="Center">
                                                            <TextBlock.Style>
                                                                <Style TargetType="TextBlock">
                                                                    <Setter Property="Foreground" Value="{StaticResource TextMutedBrush}"/>
                                                                    <Style.Triggers>
                                                                        <DataTrigger Binding="{Binding IconType}" Value="Pencil">
                                                                            <Setter Property="Text" Value="&#xE70F;"/>
                                                                            <Setter Property="Foreground" Value="{StaticResource PrimaryBrush}"/>
                                                                        </DataTrigger>
                                                                        <DataTrigger Binding="{Binding IconType}" Value="Eye">
                                                                            <Setter Property="Text" Value="&#xE18B;"/>
                                                                        </DataTrigger>
                                                                        <DataTrigger Binding="{Binding IconType}" Value="Copy">
                                                                            <Setter Property="Text" Value="&#xE8C8;"/>
                                                                        </DataTrigger>
                                                                        <DataTrigger Binding="{Binding IconType}" Value="Plus">
                                                                            <Setter Property="Text" Value="&#xE710;"/>
                                                                        </DataTrigger>
                                                                    </Style.Triggers>
                                                                </Style>
                                                            </TextBlock.Style>
                                                        </TextBlock>
                                                    </Border>
                                                    <StackPanel Grid.Column="1">
                                                        <TextBlock Text="{Binding ActionType}" Style="{StaticResource BaseText}" FontWeight="SemiBold" FontSize="13"/>
                                                        <TextBlock Text="{Binding Timestamp, StringFormat='g'}" Style="{StaticResource LabelText}" FontWeight="Normal" FontSize="11" Margin="0,2,0,0"/>
                                                    </StackPanel>
                                                </Grid>
                                            </DataTemplate>
                                        </ItemsControl.ItemTemplate>
                                    </ItemsControl>
                                </Grid>"""

content = content.replace(history_original, history_new)

with open("CipherVault/MainWindow.xaml", "w") as f:
    f.write(content)
