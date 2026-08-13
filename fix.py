import re

with open('CipherVault/MainWindow.xaml', 'r') as f:
    content = f.read()

search = '''                                                <!-- Icon Badge -->
                                                <Border Width="24" Height="24" CornerRadius="12" Background="#F1F5F9" Margin="0,0,12,0" VerticalAlignment="Top">
                                                    <TextBlock Text="•" VerticalAlignment="Center" HorizontalAlignment="Center" Foreground="{StaticResource TextMutedBrush}"/>
                                                </Border>'''
replace = '''                                                <!-- Icon Badge -->
                                                <Border Width="24" Height="24" CornerRadius="12" Background="#F1F5F9" Margin="0,0,12,0" VerticalAlignment="Top">
                                                    <TextBlock VerticalAlignment="Center" HorizontalAlignment="Center" Foreground="{StaticResource TextMutedBrush}" FontFamily="Segoe MDL2 Assets" FontSize="10">
                                                        <TextBlock.Style>
                                                            <Style TargetType="TextBlock">
                                                                <Style.Triggers>
                                                                    <DataTrigger Binding="{Binding IconType}" Value="Pencil"><Setter Property="Text" Value="&#xE70F;"/></DataTrigger>
                                                                    <DataTrigger Binding="{Binding IconType}" Value="Eye"><Setter Property="Text" Value="&#xE890;"/></DataTrigger>
                                                                    <DataTrigger Binding="{Binding IconType}" Value="Copy"><Setter Property="Text" Value="&#xE8C8;"/></DataTrigger>
                                                                    <DataTrigger Binding="{Binding IconType}" Value="Plus"><Setter Property="Text" Value="&#xE710;"/></DataTrigger>
                                                                </Style.Triggers>
                                                            </Style>
                                                        </TextBlock.Style>
                                                    </TextBlock>
                                                </Border>'''
content = content.replace(search, replace)

with open('CipherVault/MainWindow.xaml', 'w') as f:
    f.write(content)
