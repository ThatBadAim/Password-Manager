import re

with open("CipherVault/MainWindow.xaml", "r") as f:
    content = f.read()

# Make sure Search Box has search icon as requested
search_box_original = """                        <!-- Search Box -->
                        <Border Background="#F1F5F9" CornerRadius="16" Height="32" Padding="12,0" Margin="0,0,16,0" Width="200">
                            <Grid>
                                <TextBlock Text="Search vault items..." Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="24,0,0,0"/>
                                <TextBox Background="Transparent" BorderThickness="0" VerticalAlignment="Center" Text="{Binding SearchText, UpdateSourceTrigger=PropertyChanged}" Padding="24,0,0,0"/>
                            </Grid>
                        </Border>"""

search_box_new = """                        <!-- Search Box -->
                        <Border Background="#F1F5F9" CornerRadius="16" Height="32" Padding="12,0" Margin="0,0,16,0" Width="200">
                            <Grid>
                                <TextBlock Text="&#xE721;" FontFamily="Segoe MDL2 Assets" FontSize="14" Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False"/>
                                <TextBlock Text="Search vault items..." Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="24,0,0,0">
                                    <TextBlock.Style>
                                        <Style TargetType="TextBlock">
                                            <Setter Property="Visibility" Value="Hidden"/>
                                            <Style.Triggers>
                                                <DataTrigger Binding="{Binding Text.Length, ElementName=SearchTextBox, TargetNullValue=0}" Value="0">
                                                    <Setter Property="Visibility" Value="Visible"/>
                                                </DataTrigger>
                                            </Style.Triggers>
                                        </Style>
                                    </TextBlock.Style>
                                </TextBlock>
                                <TextBox x:Name="SearchTextBox" Background="Transparent" BorderThickness="0" VerticalAlignment="Center" Text="{Binding SearchText, UpdateSourceTrigger=PropertyChanged}" Padding="24,0,0,0"/>
                            </Grid>
                        </Border>"""

content = content.replace(search_box_original, search_box_new)

with open("CipherVault/MainWindow.xaml", "w") as f:
    f.write(content)
