"""
Audio processing utilities
"""
from typing import Optional
from app.core.logger import logger

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False
    logger.warning("speech_recognition not available. Audio transcription will be disabled.")


class AudioProcessor:
    """Audio processing utilities"""
    
    def __init__(self):
        if SPEECH_RECOGNITION_AVAILABLE:
            self.recognizer = sr.Recognizer()
        else:
            self.recognizer = None
    
    def transcribe_audio(self, audio_file_path: str) -> Optional[str]:
        """
        Transcribe audio file to text
        
        Args:
            audio_file_path: Path to audio file
            
        Returns:
            Transcribed text or None if failed
        """
        if not SPEECH_RECOGNITION_AVAILABLE:
            logger.error("Speech recognition library not available")
            return None
            
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data)
                return text
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Could not request results from speech recognition service: {e}")
            return None
        except Exception as e:
            logger.error(f"Error transcribing audio: {e}")
            return None
    
    def transcribe_audio_data(self, audio_data) -> Optional[str]:
        """
        Transcribe audio data to text
        
        Args:
            audio_data: Audio data
            
        Returns:
            Transcribed text or None if failed
        """
        if not SPEECH_RECOGNITION_AVAILABLE:
            logger.error("Speech recognition library not available")
            return None
            
        try:
            text = self.recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Could not request results from speech recognition service: {e}")
            return None
        except Exception as e:
            logger.error(f"Error transcribing audio: {e}")
            return None


# Global audio processor instance
audio_processor = AudioProcessor()
