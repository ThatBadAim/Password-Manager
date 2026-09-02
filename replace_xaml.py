import re

with open('/app/CipherVault/MainWindow.xaml', 'r') as f:
    content = f.read()

search = '''                                <TextBlock Text="Search vault items..." Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="24,0,0,0">
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
                                </TextBlock>'''

replace = '''                                <TextBlock Text="Search vault items..." Foreground="{StaticResource TextMutedBrush}" VerticalAlignment="Center" IsHitTestVisible="False" Margin="24,0,0,0">
                                    <TextBlock.Style>
                                        <Style TargetType="TextBlock">
                                            <Setter Property="Visibility" Value="Hidden"/>
                                            <Style.Triggers>
                                                <DataTrigger Binding="{Binding ElementName=SearchTextBox, Path=Text.Length, FallbackValue=0}" Value="0">
                                                    <Setter Property="Visibility" Value="Visible"/>
                                                </DataTrigger>
                                            </Style.Triggers>
                                        </Style>
                                    </TextBlock.Style>
                                </TextBlock>'''

content = content.replace(search, replace)

with open('/app/CipherVault/MainWindow.xaml', 'w') as f:
    f.write(content)
